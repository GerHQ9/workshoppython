teks = """ini adalah isi dari file yang akan ditulis menggunakan python"""

f = open('coba.txt', 'w')
f.write(teks)
f.close

f = open('coba.txt')
while True:
    baris = f.readline()
    if len(baris) == 0:
        break
    print (baris,)
f.close()