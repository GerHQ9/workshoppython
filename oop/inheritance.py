class AnggotaSekolah:
    "representasi anggota sekolah"
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

        print ('Membuat Anggota Sekolah baru : %s' % self.nama)

    def info(self):
        "cetak info"
        print ('Nama: %s, Umur: %s' % (self.nama,self.umur))

class Guru(AnggotaSekolah):
    "representasi guru"
    def __init__(self, nama, umur, gaji):
        AnggotaSekolah.__init__(self, nama, umur)
        self.gaji = gaji

        print ('Membuat Guru : %s' % self.nama)

    def info(self):
        AnggotaSekolah.info(self)
        print ('Gaji: %s' %self.gaji)

class Siswa(AnggotaSekolah):
    "representasi siswa"
    def __init__(self, nama, umur, nilai):
        AnggotaSekolah.__init__(self, nama, umur)
        self.nilai = nilai

        print ('Membuat Siswa: %s' % self.nama)

    def info(self):
        AnggotaSekolah.info(self)
        print ('Nilai: %s' % self.nilai)

guru = Guru('Budi', 40, 3000000)
siswa = Siswa('Andi', 25, 75)

print 

guru.info()
# anggota = [guru, siswa]

# for orang in anggota:
#     orang.info()
