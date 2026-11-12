const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const express = require('express');

const app = express();
app.use(express.json());

const client = new Client({
    authStrategy: new LocalAuth({ dataPath: './sesi_wa' }),
    puppeteer: {
        headless: true, // Tidak membuka jendela Chrome
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

// Menampilkan QR Code di Terminal untuk login
client.on('qr', (qr) => {
    console.log('\n--- SCAN QR DI BAWAH INI ---');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('\n✅ WA GATEWAY AKTIF & TERHUBUNG!');
});

// Endpoint untuk menerima perintah kirim pesan dari Django
app.post('/send-message', async (req, res) => {
    const { number, message } = req.body;
    try {
        let clean_no = number.replace(/[^0-9]/g, "");
        if (clean_no.startsWith('0')) clean_no = '62' + clean_no.slice(1);
        const chatId = clean_no + "@c.us";
        
        await client.sendMessage(chatId, message);
        console.log(`✅ Pesan Terkirim ke: ${clean_no}`);
        res.json({ status: true });
    } catch (err) {
        console.error('❌ Gagal kirim pesan:', err.message);
        res.status(500).json({ status: false, error: err.message });
    }
});

client.initialize();
app.listen(3001, () => console.log("Gateway berjalan di port 3001"));