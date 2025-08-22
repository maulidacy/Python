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
