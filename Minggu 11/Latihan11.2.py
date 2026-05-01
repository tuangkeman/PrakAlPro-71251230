b = []
while True:
    m = input("Masukkan bilangan atau done untuk selesai: ")
    if m.lower() == "done":
        break
    try:
        a = float(m)
        b.append(a)
    except ValueError:
        print("Input tidak valid, masukkan bilangan atau done")

if len(b) > 0:
    r = sum(b) / len(b)
    print()
    print("Bilangan yang dimasukkan:", b)
    print("Rata-rata               :", r)
else:
    print("Tidak ada bilangan yang dimasukkan.")