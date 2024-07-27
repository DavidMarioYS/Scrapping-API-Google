from sc_google_maps_api import ScrapeitCloudClient

# Inisialisasi klien API dengan API key
client = ScrapeitCloudClient(api_key='9fff7ecc-b454-4813-9aab-04f28fca14f5') # API dari Web Scraping API

# Kirim permintaan pencarian
response = client.scrape(
    params={
        "keyword": "Wisata Kabupaten Aceh Barat",  # Ubah keyword sesuai kebutuhan
        "country": "ID",  # Kode negara untuk Indonesia
        "domain": "com"  # Domain pencarian
    }
)

# Periksa apakah respons berhasil dan ambil data JSON
if response.status_code == 200:
    data = response.json()
    # Ambil data 'locals' dari hasil scraping
    locals = data.get('scrapingResult', {}).get('locals', [])
    
    for local in locals:
        # Ambil informasi dari setiap item
        title = local.get('title') # Menambahkan informasi nama wisata
        rating = local.get('rating') # Menambahkan informasi rating wisata
        reviews = local.get('reviews') # Menambahkan informasi reviews wisata
        type_of_tourism = local.get('type', 'Jenis wisata tidak tersedia')  # Menambahkan informasi jenis wisata
        latitude = local.get('gpsCoordinates', {}).get('latitude')
        longitude = local.get('gpsCoordinates', {}).get('longitude')
        address = local.get('address') # Menambahkan informasi lokasi wisata
        
        # Hanya proses item yang memiliki semua informasi penting dan jumlah ulasan di atas 10
        if all([title, rating, reviews, latitude, longitude, address]) and reviews > 10:
            # Mengambil nama kabupaten dari alamat
            kabupaten = address.split(",")[-3].strip() if address else "Tidak Diketahui"
            
            # Print hasil
            print(f'{title}, {rating}, {reviews}, {type_of_tourism} ,{latitude}, {longitude}, {kabupaten}')
else:
    print("Terjadi kesalahan dalam permintaan API:", response.status_code)