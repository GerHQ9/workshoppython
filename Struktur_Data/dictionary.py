ba = {'gerlandy': 'gerlandy@python.com',
      'romi' : 'romi@python.com',
      'ardian' : 'ardian@python.com'}

print ('Alamat Email romi: ', ba['romi'])

# del ba['spammer']

print ('Ada %s Kontak di Buku Alamat' % len(ba))

for nama, email in ba.items():
    print ('%s, email:%s' % (nama, email))

ba['jacob'] = 'jacob@jacobian.org'

if 'jacob' in ba:
    print ('Email Jacob di', ba['jacob'])