#program manajemen program

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=============")
        print(f"Nama : {kontak['nama']}")
        print(f"ID : {kontak['noid']}")
        print(f"Email : {kontak['email']}")
        
# menambah kontak baru
def new_kontak():
    nama = input("Nama : ")
    noid = input("ID : ")
    email = input("Email : ")
    kontak = {
        "nama" : nama,
        "noid" : noid,
        "email" : email,
    }
    return kontak

# menghapus kontak
def delete_kontak(daftar_kontak):
    ID = input("ID yang akan dihapus: ")
    
    index = -1
    
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if ID == kontak["noid"]:
            index = i
            break
        
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del daftar_kontak[index]  
        print("Data Berhasil Dihapus")
        
# mencari kontak
def search_kontak(daftar_kontak):
    name_search = input("Nama yang dicari: ")
    
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(name_search.lower()) != -1:
            print("=============")
            print(f"Nama : {kontak['nama']}")
            print(f"ID : {kontak['noid']}")
            print(f"Email : {kontak['email']}")
        