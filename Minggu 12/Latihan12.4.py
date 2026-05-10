#Minggu 12\mbox-short.txt
nama_file = input("Masukan nama file: ")

counts = {}

try:
    with open(nama_file) as f:
        for line in f:
            if line.startswith("From:"):
                parts = line.split()
                email = parts[1]
                domain = email.split("@")[1]
                counts[domain] = counts.get(domain, 0) + 1

    print(counts)

except:
    print("File cannot be opened:", nama_file)