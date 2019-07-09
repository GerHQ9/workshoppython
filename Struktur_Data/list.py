daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
len(daftar_belanja)

print ('barang tersebut : ')
for barang in daftar_belanja:
    print (barang,) 

print ('Saya Harus Membeli Beras')
daftar_belanja.append('Beras')
print ('daftar belanja sekarang : '), daftar_belanja

print ('Saya akan Mengurutkan daftar belanja saya')
daftar_belanja.sort()
print ('Daftar Belanja setelah diurutkan'), daftar_belanja

print ('Barang yang harus saya beli pertama'),
daftar_belanja[0]
barang_pertama = daftar_belanja[0]

del daftar_belanja[0]

print ('Saya Membeli', barang_pertama)
print ('Daftar Belanja Sekarang : ', daftar_belanja)
