import re
def ku(n):
    try:
        with open(f"Minggu 11/{n}", 'r') as f:
            t = f.read()
        k = re.findall(r'\b[a-zA-Z]+\b', t.lower())
        u = sorted(set(k))
        print(f"Total semua kata : {len(k)}")
        print(f"Total kata unik : {len(u)}")
        print()
        print(f"Daftar kata unik:")
        for i, kata in enumerate(u, 1):
            print(f"{i:3}. {kata}")
    except FileNotFoundError:
        print(f"File '{n}' tidak ditemukan.")
nf = input("Masukkan nama file: ")
ku(nf)