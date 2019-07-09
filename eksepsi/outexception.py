class InputPendekError(Exception):
    "Exception Jika Input terlalu pendek"

    def __init__(self, panjang, minimal):
        Exception.__init__(self)
        self.panjang = panjang
        self.minimal = minimal

try:
    teks = input('Ketikkan sesuatu: ')
    panjang = len(teks)
    minimal_panjang = 3

    if panjang < minimal_panjang:
        raise InputPendekError(panjang, minimal_panjang)
except EOFError:
    print ('\nKenapa sudah EOF?')
except KeyboardInterrupt:
    print ('\nAnda nembatalkan operasi')
except InputPendekError as e:
    print ('Input Terlalu pendek: panjang input: %s, minimal %s' %(e.panjang, e.minimal))
else:
    print ('Anda mengetikkan "%s"' % teks)
