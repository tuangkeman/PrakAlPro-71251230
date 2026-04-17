import re
from datetime import datetime

def nemutgldnhtg(k):
    tgl = re.findall(r"\d{4}-\d{2}-\d{2}", k)

    hariini = datetime.now()
    hasil = []

    for dstr in tgl:
        do = datetime.strptime(dstr, "%Y-%m-%d")

        hs = (hariini - do).days

        fd = do.strftime("%d-%m-%Y")

        hasil.append(f"{fd}{do.time()} selisih {hs} hari")

    return hasil

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""
hasil = nemutgldnhtg(teks)
for h in hasil:
    print(h)