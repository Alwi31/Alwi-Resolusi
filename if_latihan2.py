Welcome_message = "WELCOME TRAINING ALWI"
print("-------------------------")
print(f"--- {Welcome_message} ---")
print("-------------------------")
print()

print("___ Program Kasir Satu Menu Latihan ___")
print()

print("[1] Nasi Goreng  : 18000")
print("[2] Mie Ayam     : 15000")
print("[3] Ayam Geprek  : 20000")
print()

menu = int(input("Menu yg dipilih apaan der : "))
if menu == 1:
    harga = 18000
    nama_menu = "Nasi Goreng"
elif menu == 2:
    harga = 15000
    nama_menu = "Mie Ayam"
elif menu == 3:
    harga = 20000
    nama_menu = "Ayam Geprek"
else:
    print("Menu yg dipilih gak ada dherrku..")
    exit()
print()

porsi = int(input("Mao beli brpe porsi braderr ? :"))
if porsi:
    total = porsi * harga

    if porsi >= 3:
        diskon = total * 0.10
        total_setelah_diskon = total - diskon
        print(f"Karena ente beli {porsi} porsi, ente dapet diskon 10% sebesar Rp {int(diskon)}")
    else:
        diskon = 0
        total_setelah_diskon = total
        print("Ente gak dapet diskon karna gak beli 3 bungkus lebih dher wkwk.")

    print(f"Pesanan ente: {porsi} porsi {nama_menu}")
    print(f"Total bayar setelah diskon: Rp {int(total_setelah_diskon)}")
else:
    print("Terjadinya eror dherr..")

uang = int(input("Duit ente berape bang? : Rp "))
if uang >= total_setelah_diskon:
    kembalian = uang - total_setelah_diskon
    print(f"Payment sukses ye bang! nih kembalian ente Rp {kembalian:.0f}")
else:
    kurang = total_setelah_diskon - uang
    print(f"Wadohh duitnye kurang Rp {kurang:.0f} dherr... Tambahin lagi biar ente bisa bawa balik nih makanan.") 





'''if porsi:
    porsi = int(porsi)
    total = porsi * harga
    if porsi >= 3:
        diskon = total * 0.10
        total -= diskon
    else:
        print("Ente gak dapet diskon karna gak beli 3 bungkus lebih dher wkwk.")
    print(f"ente jadinye beli {menu} {porsi} porsi")
    print(f"Nah, trus ente dapet diskon Rp {diskon} karna ente beli banyakan derr. Total di diskon jadi Rp {total}")
    print(f"Jadi total yg harus ente bayar Rp {total:.0f}")
else:'''