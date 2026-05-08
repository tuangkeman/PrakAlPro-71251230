nama_file = input("Masukkan nama file : ")
#Minggu 12\mbox-short.txt
counts = {}

try:
    with open(nama_file) as f:
        lines = f.readlines()

    for line in reversed(lines):
        if line.startswith("From "):
            parts = line.split()
            email = parts[1]
            domain = email.split("@")[1]
            counts[domain] = counts.get(domain, 0) + 1

except FileNotFoundError:
    print("File tidak ditemukan")
    exit()

print(counts)