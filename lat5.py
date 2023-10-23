def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil penambahan:", hasil)

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print("Hasil penambahan:", hasil)

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil penambahan:", hasil)

def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak bisa dibagi oleh 0"
    hasil = angka1 / angka2
    print("Hasil penambahan:", hasil)
# Menu interaktif
while True:
    print("Pilih operasi kalkulator:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih! Aplikasi kalkulator selesai.")
        break

    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid. Silakan masukkan nomor operasi yang benar.")
        continue

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
       tambah(angka1,angka2)
    elif pilihan == '2':
       kurang(angka1,angka2)
    elif pilihan == '3':
       kali(angka1,angka2)
    elif pilihan == '4':
        bagi(angka1,angka2)

