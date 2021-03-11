print("===== Menghitung Luas Persegi Panjang =====")
panjang = float(input("Masukkan panjang :"))
lebar = float(input("Masukkan lebar :"))
luas = (panjang*lebar)
print("Luas persegi panjang adalah",luas,"satuan")

print("===== Menghitung Luas Lingkaran =====")
phi = 3.14
jari_jari = float(input("Masukkan jari-jari :"))
luas = jari_jari*jari_jari*phi
print("Luas lingkaran adalah",luas,"satuan")

print("===== Menghitung Luas Kubus =====")
sisi = float(input("Masukkan sisi :"))
luas_permukaan = 6*sisi*sisi
print("Luas permukaan kubus adalah",luas_permukaan,"satuan")

print("===== Menghitung Konversi Suhu dari Celcius ke Fahrenheit")
celcius = float(input("Masukkan suhu celcius :"))
konversi = (((9/5)*celcius)+32)
print("Konversi suhu dari celcius ke fahrenheit adalah",konversi,"derajat")

print("Menghitung konversi suhu dari reamur ke kelvin")
reamur = float(input("Masukkan suhu reamur :"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu dari reamur ke kelvin adalah",konversi,"derajat")