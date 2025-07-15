#------------------------- 1. Login Sederhana -------------------------
huruf = input("Masukan 1 huruf : ") 
huruf_vokal = "a e i o u A E I O U"

if huruf in huruf_vokal:
    print(f"Ya, huruf {huruf} adalah huruf vokal")
else:  
    print(f"Tidak, huruf {huruf} bukan huruf vokal")