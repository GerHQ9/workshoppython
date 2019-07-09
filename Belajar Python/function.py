def halo_dunia():
    print ('Halo Dunia')

halo_dunia()

nama = input('Masukkan Nama Kamu : ')

def halo(nama):
    
    print ('Halo %s' % nama)

halo(nama)

def cetak_maksimal(a, b):

    if a > b :
        print('%s lebih besar dari %s' % (a,b))
    elif a == b :
        print('%s sama dengan %s' %(a,b))
    else :
        print ('%s lebih kecil dari %s' %(a,b))
    
# cetak_maksimal(10, 100)

a = input('Masukkan Nilai A : ')
b = input('Masukkan Nilai B : ')

cetak_maksimal(a, b)


x = 56

def fungsi(x):
    print ('x - ', x)
    x = 2
    print ('Merubah Lokal Variabel x = ', x)

fungsi(100)

print  ('Nilai x masih %s ' % x)

x = 50

def fungsi():
    print ('x = ', x)

def fungsi2():
    x = 100
    print ('x = ', x)

def fungsi3():
    global x
    x = 100
    print ('x - ', x)

fungsi()
print ('nilai x = ', x)

fungsi2()
print ('nilai x = ', x)

fungsi3()
print ('nilai x = ', x)

def katakan(pesan, jumlah=1):
    print (pesan * jumlah)

katakan('Halo ')
katakan('Halo ', 3)

def fungsi(a, b=5, c=10):
    print ('a = ', a)
    print ('b = ', b)
    print ('c = ', c)

fungsi(3, 7, 11)
fungsi(25, c=24)
fungsi(c=50 , a=100)

def total(*bilangan, **keywords):
    hitung = 0
    for bil in bilangan:
        hitung += bil
    for key in keywords:
        hitung += keywords[key]
    return hitung

print (total(1, 2, 3, 4, 5))
print (total(daging=2, sayur=3, buah=4))
print (total(7, 8, 5, daging=2, sayur=3, buah=4))

def katakan(pesan, jumlah=1):
    ("mencetak pesan (pesan) dengan jumlah (jumlah)")
    print (pesan * jumlah)

print (katakan.__doc__)