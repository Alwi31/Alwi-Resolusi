Welcome_message = "WELCOME TRAINING ALWI"
print("-------------------------")
print(f"--- {Welcome_message} ---")
print("-------------------------")

print("---Latihan if abang warteg---")
print("Daftar Menu Warteg : ")
print("[1] Bakso = 20000/porsi", "[2] Sate Ayam = 25000/porsi", "[3] Soto Mie = 15000/porsi")
print("[0] Selesai pesan.")

total_harga = 0 # total semua makanan
pesanan = []    # buat simpan list pesanan

while True:
    menu = int(input("Mau menu yg nomor berapa (0 untk selesai) : "))

    if menu == 0:
        break
    elif menu == 1:
        harga = 20000
        makanan = "Bakso"
    elif menu == 2:
        harga = 25000
        makanan = "Sate Ayam"
    elif menu == 3:
        harga = 15000
        makanan = "Soto Mie"
    else:
        print("Menu tidak tersedia, coba lagi menu yg laen dherr..")
        continue

    porsi = int(input(f"Mao beli berape porsi dher {makanan} : "))
    subtotal = harga*porsi
    total_harga += subtotal
    pesanan.append(f"{porsi} porsi {makanan} = {subtotal}")

    print(f"{makanan} ditambah ke pesanan. Subtotal : {subtotal}\n")

print("\n--- Ringkasan Pesanan Awing adalah ---")
for item in pesanan:
    print(item)
print(f"Total yg harus dibayar awing : {total_harga}")

bayar = int(input("Jumlah yang harus dibayarkan : "))

if bayar >= total_harga:
    kembalian = bayar - total_harga
    print(f"Pembayaran berhasil. Kembalian : {kembalian}")
else:
    kurang = total_harga - bayar
    print(f"Uang kurang {kurang}. Silahkan tambahin uang nye der..")