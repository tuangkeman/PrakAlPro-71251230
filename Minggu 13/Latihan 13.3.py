file = input("Enter a file name: ")

c = dict()

try:
    fop = open(file)
    for line in fop:
        if not line.startswith("From "):
            continue
        kata = line.split()
        wektu = kata[5]
        jam = wektu.split(":")[0]
        c[jam] = c.get(jam, 0) + 1

    for jam in sorted(c):
        print(jam, c[jam])

except FileNotFoundError:
    print("File tidak ditemukan:", file)