def bandingkan_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        li1 = f1.readlines()
        li2 = f2.readlines()

    ml = max(len(li1), len(li2))

    for i in range(ml):
        baris1 = li1[i].strip() if i < len(li1) else ''
        baris2 = li2[i].strip() if i < len(li2) else ''

        if baris1 != baris2:
            print(f"Perbedaan di baris {i+1}:")
            print(f"  File 1: {baris1}")
            print(f"  File 2: {baris2}\n")

# Test Case
bandingkan_file('Minggu 10/file1.txt', 'Minggu 10/file2.txt')