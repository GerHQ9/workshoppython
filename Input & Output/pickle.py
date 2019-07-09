import pickle

daftar_belanja_file = 'daftar.data'
daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']


f = open(daftar_belanja_file, 'wb')

pickle.dump(daftar_belanja, f)
f.close()

del daftar_belanja

f = open(daftar_belanja_file, 'rb')
daftar_tersimpan = pickle.load(f)
print (daftar_tersimpan)