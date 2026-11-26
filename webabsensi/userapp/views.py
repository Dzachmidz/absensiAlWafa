from django.shortcuts import render
from django.utils import timezone
from .models import Absensi, Siswa, RfidLog, WaktuOperasional, JadwalSesi
import datetime
import requests
import json
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RfidScanSerializer

def kirim_wa_gateway(number, message):
    url = "http://localhost:3001/send-message"
    data = {"number": str(number), "message": message}
    try:
        response = requests.post(url, json=data, timeout=5)
        return response.status_code == 200
    except Exception as e:
        print(f"DEBUG: Koneksi ke Node.js Gagal: {e}")
        return False

# ... (bagian import tetap sama) ...

class RfidScanView(APIView):
    def post(self, request):
        serializer = RfidScanSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data['uid']
            now_aware = timezone.localtime(timezone.now())
            current_time = now_aware.time()
            today = now_aware.date()
            time_str = current_time.strftime('%H:%M')

            try:
                siswa = Siswa.objects.select_related('kelas').get(rfid_uid=uid)
            except Siswa.DoesNotExist:
                RfidLog.objects.create(
                    rfid_uid=uid,
                    status='unknown',
                    keterangan=f"Kartu tidak dikenal scan pada {time_str}"
                )
                return Response({
                    "status": "error",
                    "code": "unregistered",
                    "message": "Kartu Tidak Terdaftar"
                }, status=status.HTTP_404_NOT_FOUND)

            nama_kelas = str(siswa.kelas) if siswa.kelas else "-"
            kelas_siswa = siswa.kelas

            # Dapatkan jadwal batas absen (Mendukung sesi jika ada, atau default jadwal kelas)
            sessions = kelas_siswa.sesi_jadwal.all() if kelas_siswa else []
            active_session = None

            # 1. Cek apakah ada sesi jadwal
            if sessions:
                # Cari sesi yang paling relevan dengan waktu sekarang
                for ses in sessions:
                    if ses.jam_masuk_mulai <= current_time <= ses.jam_pulang_akhir:
                        active_session = ses
                        break
                if not active_session:
                    # Cari sesi terdekat jika di luar rentang
                    valid_candidates = [s for s in sessions if s.jam_masuk_mulai <= current_time]
                    if valid_candidates:
                        valid_candidates.sort(key=lambda x: x.jam_masuk_mulai, reverse=True)
                        active_session = valid_candidates[0]
                    else:
                        active_session = sessions.first()

            # Tentukan batas waktu
            if active_session:
                j_masuk_mulai = active_session.jam_masuk_mulai
                j_masuk_akhir = active_session.jam_masuk_akhir
                j_pulang_mulai = active_session.jam_pulang_mulai
                j_pulang_akhir = active_session.jam_pulang_akhir
                sesi_obj = active_session
            elif kelas_siswa:
                j_masuk_mulai = kelas_siswa.jadwal_masuk_mulai
                j_masuk_akhir = kelas_siswa.jadwal_masuk_akhir
                j_pulang_mulai = kelas_siswa.jadwal_pulang_mulai
                j_pulang_akhir = kelas_siswa.jadwal_pulang_akhir
                sesi_obj = None
            else:
                # Fallback Waktu Operasional jika belum ada kelas
                waktu_op = WaktuOperasional.get_solo()
                j_masuk_mulai = waktu_op.jam_masuk_mulai
                j_masuk_akhir = waktu_op.jam_masuk_akhir
                j_pulang_mulai = waktu_op.jam_pulang_mulai
                j_pulang_akhir = waktu_op.jam_pulang_akhir
                sesi_obj = None

            # Cek riwayat absensi siswa hari ini
            open_absensi = Absensi.objects.filter(
                siswa=siswa,
                tanggal=today,
                jam_keluar__isnull=True
            ).first()

            # ==========================================
            # KASUS A: SUDAH ABSEN MASUK -> PROSES PULANG
            # ==========================================
            if open_absensi:
                # Cek batas mulai pulang
                if current_time < j_pulang_mulai:
                    jam_mulai_str = j_pulang_mulai.strftime('%H:%M')
                    jam_masuk_str = open_absensi.jam_masuk.strftime('%H:%M') if open_absensi.jam_masuk else "-"
                    msg = f"Sudah absen masuk jam {jam_masuk_str}. Belum waktunya pulang (Mulai jam {jam_mulai_str})."
                    return Response({
                        "status": "warning",
                        "code": "too_early_leave",
                        "nama": siswa.nama,
                        "kelas": nama_kelas,
                        "waktu": time_str,
                        "mode": "Peringatan",
                        "message": msg
                    }, status=status.HTTP_200_OK)

                # Sudah masuk waktu pulang
                status_keterangan = "Pulang"
                if current_time > j_pulang_akhir:
                    keterangan_pulang = "Telat Jemput"
                    status_kehadiran_update = f"{open_absensi.status_kehadiran} (Telat Jemput)"
                else:
                    keterangan_pulang = "Tepat Waktu"
                    status_kehadiran_update = open_absensi.status_kehadiran

                open_absensi.jam_keluar = current_time
                if "Telat Jemput" in status_kehadiran_update and "Telat Jemput" not in open_absensi.status_kehadiran:
                    open_absensi.status_kehadiran = status_kehadiran_update
                open_absensi.save()

                # Log RFID
                RfidLog.objects.create(
                    rfid_uid=uid,
                    status='success',
                    keterangan=f"Absen Pulang: {siswa.nama} ({keterangan_pulang}) - {time_str}"
                )

                # Kirim WA Gateway
                nomor_hp = getattr(siswa, 'no_telepon', None)
                if nomor_hp:
                    isi_wa = f"Halo, {siswa.nama} berhasil absen Pulang jam {time_str} ({keterangan_pulang})."
                    kirim_wa_gateway(nomor_hp, isi_wa)

                return Response({
                    "status": "success",
                    "nama": siswa.nama,
                    "kelas": nama_kelas,
                    "waktu": time_str,
                    "mode": "Pulang",
                    "detail_status": keterangan_pulang,
                    "message": f"Berhasil Absen Pulang ({keterangan_pulang})"
                }, status=status.HTTP_200_OK)

            # ==========================================
            # KASUS B: BELUM ABSEN MASUK -> PROSES MASUK
            # ==========================================
            # Cek apakah sudah pernah absen lengkap hari ini (masuk & pulang selesai)
            absen_selesai = Absensi.objects.filter(
                siswa=siswa,
                tanggal=today,
                jam_keluar__isnull=False
            ).first()
            if absen_selesai:
                return Response({
                    "status": "info",
                    "code": "already_completed",
                    "nama": siswa.nama,
                    "kelas": nama_kelas,
                    "waktu": time_str,
                    "mode": "Selesai",
                    "message": f"{siswa.nama} sudah menyelesaikan absensi masuk dan pulang hari ini."
                }, status=status.HTTP_200_OK)

            # Validasi apakah terlalu awal sebelum batas absen masuk
            if current_time < j_masuk_mulai:
                jam_buka_str = j_masuk_mulai.strftime('%H:%M')
                msg = f"Belum waktunya absen masuk. Absen masuk dibuka jam {jam_buka_str}."
                return Response({
                    "status": "warning",
                    "code": "too_early_entry",
                    "nama": siswa.nama,
                    "kelas": nama_kelas,
                    "waktu": time_str,
                    "mode": "Peringatan",
                    "message": msg
                }, status=status.HTTP_200_OK)

            # Tentukan status kehadiran masuk (Tepat Waktu vs Terlambat)
            if current_time <= j_masuk_akhir:
                status_kehadiran = "Tepat Waktu"
            else:
                status_kehadiran = "Terlambat"

            # Buat record absensi masuk
            Absensi.objects.create(
                siswa=siswa,
                tanggal=today,
                jam_masuk=current_time,
                hari=now_aware.strftime("%A"),
                status_kehadiran=status_kehadiran,
                sesi=sesi_obj
            )

            # Log RFID
            RfidLog.objects.create(
                rfid_uid=uid,
                status='success',
                keterangan=f"Absen Masuk: {siswa.nama} ({status_kehadiran}) - {time_str}"
            )

            # Kirim WA Gateway
            nomor_hp = getattr(siswa, 'no_telepon', None)
            if nomor_hp:
                isi_wa = f"Halo, {siswa.nama} berhasil absen Masuk jam {time_str} ({status_kehadiran})."
                kirim_wa_gateway(nomor_hp, isi_wa)

            return Response({
                "status": "success",
                "nama": siswa.nama,
                "kelas": nama_kelas,
                "waktu": time_str,
                "mode": "Masuk",
                "detail_status": status_kehadiran,
                "message": f"Berhasil Absen Masuk ({status_kehadiran})"
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rfid_feedback_view(request):
    # Tampilan layar RFID. Jangan pakai bare except: dulu error asli tertutup
    # dan jatuh ke template yang tidak ada (rfid_feedback.html).
    return render(request, 'user.html')