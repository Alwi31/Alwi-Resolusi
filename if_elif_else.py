Welcome_message = "WELCOME TRAINING ALWI"
ALWI_posisi = random.randint(1, 4)
print("-------------------------")
print(f"--- {Welcome_message} ---")
print("-------------------------")

#if (kondisi)

print("Bakso = 20000/porsi", "Sate ayam = 25000/porsi", "Soto mie = 15000/porsi")
print("[1] Bakso", "[2] Sate ayam", "[3] Soto mie")

awing = int(input("Makanan nomor berapa yang mau dibeli : "))
if awing == 1:
    harga = 20000
    jenis_makanan = "Bakso"
    print("awing pilih makan bakso.")
elif awing == 2:
    harga = 25000
    jenis_makanan = "Sate ayam"
    print("awing pilih makan sate ayam.")
elif awing == 3:
    harga = 15000
    jenis_makanan = "Soto mie"
    print("awing pilih makan soto mie.")
else:
    print("makanan yang dipilih tidak tersedia")
exit()

jumlah_porsi = int(input("Mau beli berapa porsi : "))
if jumlah_porsi:
    jumlah_porsi = int(jumlah_porsi)
    total = jumlah_porsi*harga
    print(f"awing beli {jumlah_porsi} porsi {jenis_makanan} dengan total harga {total}")
else:
    print("Makanan tidak ada dalam daftar yg ingin dipilih")