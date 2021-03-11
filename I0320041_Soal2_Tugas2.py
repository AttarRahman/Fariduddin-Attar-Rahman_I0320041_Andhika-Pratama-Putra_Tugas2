# biodata
nama = "Fariduddin Attar Rahman"
nim = "I0320041"
jenis_kelamin = "Laki-laki"
prodi = "Teknik Industri"
angkatan = 2020
tempat_lahir = "Bojonegoro"
tgl_lahir = "4 Juli 2002"

# umur
tlahir = 4
blahir = 7
ylahir = 2002
lahir = tlahir+(blahir*30)+(ylahir*365)
tsekarang = 11
bsekarang = 3
ysekarang = 2021
sekarang = tsekarang+(bsekarang*30)+(ysekarang*365)
tahun = int((sekarang-lahir)/365)
bulan = int(((sekarang-lahir)%365)/30)
hari = int(((sekarang-lahir)%365)%30)

# alamat dan lingkungan tempat tinggal
alamat = "Jl.Elang C1-12 Perum UNS V Palur, Ngringo, Jaten, Karanganyar"
lingkungan = "Rumah saya berada di perumahan tetapi dekat dengan sawah yang hijau"

# informasi tambahan
berat_badan = 53
tinggi_badan = 177
uk_sepatu = 43
us_sepatu = 9.5
makanan_favorit = "Mie goreng"
minuman_favorit = "Es teh"
software ="Autodesk Inventor (cakap) dan Adobe Photoshop (basic)"
hobi = "Futsal,Belajar,Membaca buku"

# tampilkan semua informasi di layar
print("Nama :",nama)
print("NIM  :",nim)
print("Jenis kelamin :",jenis_kelamin)
print("Alamat :",alamat)
print("Saya adalah seorang mahasiswa",prodi,"angkatan",angkatan)
print("Saya lahir di",tempat_lahir,"pada",tgl_lahir,"dan sekarang berumur",tahun,"tahun",bulan,"bulan",hari,"hari")
print(lingkungan)
print("Hobi saya adalah",hobi)
print("Berat badan saya",berat_badan,"kg, dan","tinggi saya",tinggi_badan,"cm")
print("Ukuran sepatu saya UK",uk_sepatu,"atau US",us_sepatu)
print("Makanan favorit saya",makanan_favorit,"ditemani dengan",minuman_favorit)
print("Saya memiliki skill software",software)