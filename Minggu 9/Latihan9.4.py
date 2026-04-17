import re

def cekombak(n):
    hasil = re.findall(r"\w+",n)
    pendek = min(hasil, key=len)
    panjang = max(hasil, key=len)
    return panjang, pendek

kalimat = "red snakes and a black frog in the pool"

p, pe = cekombak(kalimat)

print(f" terpendek: {pe},terpanjang: {p}")