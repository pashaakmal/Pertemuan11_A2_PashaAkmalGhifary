def hitung_angka_dibagi(daftar_angka, pemisah):
    total = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            total += angka
    print(total)
hitung_angka_dibagi([10,20,45,23],2)