nomor_acak = 7
print ('tebak nomor acak dari 1 - 10')

tebakan = int(input('Tebakan anda (bil_bulat): '))

if tebakan == nomor_acak:
    print('Selamat Tebakan Anda Benar')
    print('Gak dapat Hadiah :(')
elif tebakan < nomor_acak:
    print('Selamat Tebakan Anda terlalu Kecil')
else :
    print ('Tebakan anda terlalu Besar')

print ('selesai')


for i in range(1, 6):
    print (i)
else:
    print ('Perulangan Telah Selesai')

while True:
    data = input('Masukkan Sesuatu : ')
    if data == ('keluar'):
        break
    print ('Inputan Penggunan "%s"' % data)
print ('Selesai')

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print (i)