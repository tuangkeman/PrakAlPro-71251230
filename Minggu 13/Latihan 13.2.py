d = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

jeneng = d[0]
nim  = d[1]
dodos = d[2]

print("Data: ", d)
print()
print("NIM    :", nim)
print("NAMA   :", jeneng)
print("ALAMAT :", dodos)
print()

nt = tuple(nim)
print("NIM:", nt)
print()

jenngarep = jeneng.split()[0]
ndt = tuple(jenngarep)
print("NAMA DEPAN:", ndt)
print()

walik = tuple(reversed(jeneng.split()))
print("NAMA TERBALIK:", walik)