import re
def tt(data):
    data = sorted(list(map(int,data)), reverse=True)
    return data[:3]

nilai = input("Masukan bilangan list :")
nilai = re.findall(r'\d+', nilai)

hasil = tt(nilai)
print("List inputan    :", list(map(int,nilai)))
print("3 nilai terbaik:", list(map(int,hasil)))