# Chatbot Manajemen Hubungan Pelanggan Rudy Salon & Spa

Chatbot ini dirancang untuk membantu manajemen hubungan pelanggan di Rudy Salon & Spa dengan menyediakan informasi layanan, harga, jadwal operasional, cara reservasi, promo, lokasi, produk, dan metode pembayaran.

## Fitur Utama

- **Greeting**: Menyambut pelanggan yang datang dengan sapaan yang ramah.
- **Layanan**: Memberikan informasi tentang layanan yang tersedia di Rudy Salon & Spa.
- **Harga**: Memberikan informasi tentang harga perawatan dan layanan yang tersedia.
- **Jadwal**: Memberikan informasi tentang jam operasional Rudy Salon & Spa.
- **Kontak**: Memberikan nomor telepon untuk menghubungi Rudy Salon & Spa.
- **Reservasi**: Memfasilitasi proses reservasi untuk layanan perawatan.
- **Promo**: Memberikan informasi tentang promo dan diskon yang tersedia.
- **Karyawan**: Memberikan informasi tentang jumlah dan jenis staf yang tersedia di Rudy Salon & Spa.
- **Lokasi**: Menyediakan alamat lengkap Rudy Salon & Spa.
- **Produk**: Menyediakan informasi tentang produk yang dijual di Rudy Salon & Spa.
- **Metode Pembayaran**: Menyediakan informasi tentang metode pembayaran yang diterima.

## Struktur Data

Data percakapan disusun menggunakan **intent-based framework** dengan beberapa intent utama, termasuk:

- `no_data`: Menangani input yang tidak dikenali.
- `greeting`: Menangani sapaan dan ucapan selamat datang.
- `goodbye`: Menangani perpisahan atau ucapan selamat tinggal.
- `terimakasih`: Menangani ucapan terima kasih.
- `salam`: Menangani salam seperti "Assalamualaikum".
- `layanan`: Menangani permintaan informasi tentang layanan.
- `harga`: Menangani pertanyaan tentang harga layanan.
- `jadwal`: Menangani pertanyaan tentang jam operasional.
- `kontak`: Menangani permintaan informasi kontak.
- `reservasi`: Menangani permintaan untuk melakukan reservasi.
- `promo`: Menangani pertanyaan tentang promo dan diskon.
- `karyawan`: Menangani permintaan informasi tentang jumlah staf.
- `lokasi`: Menangani pertanyaan tentang lokasi atau alamat.
- `produk`: Menangani permintaan informasi tentang produk yang dijual.
- `metode_pembayaran`: Menangani pertanyaan tentang metode pembayaran.

## Instalasi

### Persyaratan

- Python 3.x
- Library Python untuk NLP (Natural Language Processing), seperti `nltk` atau `spaCy`
- JSON untuk menyimpan data percakapan (optional, Anda bisa menggunakan format lain seperti database)

### Langkah-langkah Instalasi

1. Clone repositori ini ke mesin lokal Anda.

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Masuk ke direktori proyek.

   ```bash
   cd chatbot-rudy-salon
   ```

3. Install dependencies yang diperlukan.

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan chatbot.
   ```bash
   python app.py
   ```

## Penggunaan

1. **Mulai Percakapan**: Ketikkan sapaan seperti "Halo" atau "Hi" untuk memulai percakapan.
2. **Tanya tentang layanan**: Tanyakan tentang layanan yang tersedia di salon seperti "Apa saja layanan di sini?".
3. **Tanya harga**: Tanyakan tentang harga perawatan atau layanan, misalnya "Berapa harga facial?".
4. **Reservasi**: Anda dapat melakukan reservasi dengan menyebutkan layanan yang ingin dipilih dan waktu yang diinginkan.
5. **Informasi promo**: Tanyakan tentang promo dan diskon yang sedang berlangsung di salon.

## Kontribusi

Kami sangat menghargai kontribusi dari komunitas! Jika Anda ingin memperbaiki atau menambah fitur, silakan fork repositori ini dan buat pull request. Pastikan untuk mengikuti panduan kode yang ada.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
