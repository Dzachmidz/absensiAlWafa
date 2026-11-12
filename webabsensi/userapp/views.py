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
            try:
                siswa = Siswa.objects.get(rfid_uid=uid)
                now_aware = timezone.localtime(timezone.now())
                current_time = now_aware.strftime('%H:%M')
                today = now_aware.date()
                
                # Logika Absensi
                open_absensi = Absensi.objects.filter(siswa=siswa, tanggal=today, jam_keluar__isnull=True).first()
                msg_status = "Masuk"
                if open_absensi:
                    open_absensi.jam_keluar = now_aware.time()
                    open_absensi.save()
                    msg_status = "Pulang"
                else:
                    Absensi.objects.create(siswa=siswa, tanggal=today, jam_masuk=now_aware.time(), hari=now_aware.strftime("%A"), status_kehadiran="Hadir")

                # Ambil Nama Kelas
                nama_kelas = str(siswa.kelas) if siswa.kelas else "-"
                
                # Kirim WA (Logic tetap sama)
                nomor_hp = getattr(siswa, 'no_telepon', None)
                if nomor_hp:
                    isi_wa = f"Halo, {siswa.nama} berhasil absen {msg_status} jam {current_time}"
                    kirim_wa_gateway(nomor_hp, isi_wa)

                # RESPONSE UNTUK TAMPILAN (PENTING!)
                return Response({
                    "status": "success",
                    "nama": siswa.nama,
                    "kelas": nama_kelas,
                    "waktu": current_time,
                    "mode": msg_status
                }, status=status.HTTP_200_OK)

            except Siswa.DoesNotExist:
                return Response({"status": "error", "message": "Kartu Tidak Terdaftar"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rfid_feedback_view(request):
    try:
        return render(request, 'user.html')
    except:
        return render(request, 'rfid_feedback.html')