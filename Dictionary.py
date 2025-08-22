# "key": "value" adalah format dari dictionary
# Dictionary adalah tipe data yang menyimpan data dalam bentuk pasangan key-value.  
# Key bersifat unik, artinya tidak boleh ada key yang sama dalam satu dictionary.
# Nilai dari key bisa berupa tipe data apa saja, termasuk string, integer, list, atau bahkan dictionary itu sendiri.
# Untuk mengakses nilai, kita menggunakan key yang sesuai.

# ----------------------------------------------------------------------------------------------------------------
mahasiswa = {
    "nama": "Maul",
    "umur": 20,
    "jurusan": "Teknik Informatika"
}

#cetak hanya nama
print(mahasiswa["nama"])

#tambah data baru
mahasiswa["angkatan"] = 2023
print(mahasiswa)

#ubah data
mahasiswa["umur"] = 21

#hapus data
del mahasiswa["jurusan"]
print(mahasiswa)
exit()

#-------------------------------------------------- membuat dict --------------------------------------------------
produk = {
    "nama": "Roti", 
    "harga": 15000, 
    "stok": 20
}

# ambil data
print(produk["nama"])   # Roti

# tambah data
produk["kategori"] = "Makanan"

# ubah data
produk["stok"] = 15

# hapus data
del produk["harga"]

# cek key ada atau tidak
print("stok" in produk)   # True
