Tentu, saya akan memparafrase dan menerjemahkan konten tersebut ke dalam bahasa Indonesia dengan struktur dan alur yang sesuai untuk README. Berikut hasilnya:

# API Google Maps

[Scrapeit Cloud](https://scrape-it.cloud/) - API Web Scraping dengan Rotasi Proxy. Dapatkan data berharga dalam skala besar dalam format HTML dari situs web mana pun tanpa perlu proxy.

Antarmuka untuk memanggil [Google Maps Scraper](https://scrape-it.cloud/google-maps-scraper) dengan mudah menggunakan Python.

## Instalasi

Pasang paket menggunakan pip:

```
pip install sc-google-maps-api
```

## Penggunaan

Daftar ke Scrapeit Cloud untuk [mendapatkan kunci API Anda](https://app.scrape-it.cloud/sign-up) dan beberapa kredit gratis untuk memulai.

```python
from sc_google_maps_api import ScrapeitCloudClient

# Inisialisasi klien
client = ScrapeitCloudClient(api_key='MASUKKAN_KUNCI_API_ANDA_DI_SINI')

# Melakukan scraping
response = client.scrape(
    params={
        "keyword": "tukang ledeng di jakarta",
        "country": "ID",
        "domain": "co.id"
    }
)

# Menampilkan hasil
print(response.text)
```

Hasil akan berupa string JSON yang berisi informasi tentang tukang ledeng di Jakarta, termasuk nama, nomor telepon, alamat, situs web, peringkat, jumlah ulasan, dan jenis usaha.

Anda dapat menemukan semua parameter yang didukung di [dokumentasi Scrapeit Cloud](https://scrape-it.cloud/docs/).

---

Penjelasan tambahan:
- API ini memungkinkan Anda untuk mengambil data dari Google Maps secara otomatis.
- Anda perlu mendaftar di Scrapeit Cloud untuk mendapatkan kunci API.
- Permintaan scraping dilakukan dengan menentukan kata kunci, negara, dan domain.
- Hasil scraping akan berupa data JSON yang berisi informasi bisnis yang relevan.
- API ini berguna untuk mengumpulkan data bisnis lokal dalam jumlah besar dari Google Maps.

Pastikan untuk mematuhi syarat dan ketentuan penggunaan API serta kebijakan Google Maps saat menggunakan layanan ini.