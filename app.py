# Import module
import module

# buat list dalam dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Renaldi",
    "noid" : "180322",
    "email" : "renaldi@gmail.com"})

#Menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")
    
    menu = input("Pilih Menu: ")
    
    if menu == "0":
        break
    elif menu == "1":
        module.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = module.new_kontak() 
        daftar_kontak.append(kontak)
    elif menu =="3":
        module.delete_kontak(daftar_kontak)
    elif menu =="4":
        module.search_kontak(daftar_kontak)
    else:
        print("Input ditolak")
        
print("Program selesai, Bye!")
