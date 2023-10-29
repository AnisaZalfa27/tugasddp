a = ["896894", "beat", "100", "merah"]
a.append("200 juta")
print(a)
a.insert(2, "honda")
a.insert(3, "matic")

ket = '''selamat datang di aplikasi menghitung luas bangun datar, masukkan pilihan:
1. luas persegi
2. luas lingkaran
3. luas segitiga
'''

pilihan = input(ket)
match pilihan:
    
case "1":
print("kamu memilih 1 untuk menghitung luas persegi")
sisi = int(input("masukkan sisi:"))
luasP= sisi * sisi
print("luas persegi yang sisinya ", sisi, "adalah", luasP)

case "2":
print("kamu memilih 2 untuk menghitung luas lingkaran")
jari2 = float(input("masukkan jari2:"))
luasL = 3.14 * jari2 * jari2
print("luas lingkaran yang jari2nya", jari2, "adalah", int(luasL))

case "3":
print("kamu memilih 3 untuk menghitung luas segitiga")
alas = int(input("masukkan alas:"))
tinggi = int(input ("masukkan tinggi:"))
luasS = 0.5 * alas * tinggi
print ("luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah", int(luasS))

case_ :
print("salah memilih pilihan")
