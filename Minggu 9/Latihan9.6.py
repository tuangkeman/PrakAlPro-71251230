import re
import random
import string

def gpw(length=8):
    huruf = string.ascii_letters + string.digits
    return ''.join(random.choice(huruf) for _ in range(length))

def egpw(text):
    # Cari semua email
    emil = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    
    results = []
    for email in emil:
        # Ambil username sebelum '@'
        username = email.split('@')[0]
        
        # Generate password random 8 karakter
        password = gpw()
        
        # Simpan hasil
        results.append(f"{email} username: {username} , password: {password}")
        
    return results

# Contoh penggunaan
teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

hasil = egpw(teks)
for h in hasil:
    print(h)