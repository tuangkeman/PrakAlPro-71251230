nama_file = input("Masukkan nama file : ")
#Minggu 12\mbox-short.txt
counts = {}

with open(nama_file) as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("From "):
        parts = line.split()
        email = parts[1]
        counts[email] = counts.get(email, 0) + 1

print(counts)