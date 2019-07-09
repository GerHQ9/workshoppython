try:
    teks = input('Ketikkan sesuatu: ')
except EOFError:
    print ('\nKenapa sudah EOF? ')
except KeyboardInterrupt:
    print('\nAnda Membatalkan operasi')
else:
    print('Anda mengetikkan "%s"' % teks)