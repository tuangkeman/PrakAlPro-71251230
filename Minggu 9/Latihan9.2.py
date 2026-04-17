import re

def count_word_occurrences(kal, kat):
    pola = r'\b' + re.escape(kat) + r'\b'
    
    ksat = re.findall(pola, kal, flags=re.IGNORECASE)
    return len(ksat)

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata_dicari = "makan"
jumlah = count_word_occurrences(kalimat, kata_dicari)

print(f"{kata_dicari} ada {jumlah} buah")