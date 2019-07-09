bilangan1 = 5
bilangan2 = 3

print ('bil1 = ', (bilangan1))
print ('bil2 = ', (bilangan2))

print ('bil1 + bil2 = ', (bilangan1 + bilangan2))
print ('bil1 - bil2 = %s'% (bilangan1 - bilangan2))
print ('bil1 * bil2 = '.format (bilangan1 * bilangan2))
print ('bil1 ** bil2 = ', (bilangan1 ** bilangan2))

bilangan1 = 5.0
bilangan2 = 3.0
print ('bil1 = ', (bilangan1))
print ('bil2 = ', (bilangan2))

print ('bil1 / bil2 = ',(bilangan1 / bilangan2))
print ('bil1 // bil2 = ',(bilangan1 // bilangan2))
print ('bil1 % bil2 = ',(bilangan1 % bilangan2))

print ('-' * 80)

bilangan1 = 5
bilangan2 = 3

print ('bil1 = '), bilangan1
print ('bil2 = '), bilangan2

print ('bil1 << bil2 = ', (bilangan1 << bilangan2))
print ('bil1 >> bil2 = ', (bilangan1 >> bilangan2))
print ('bil1 & bil2 = ', (bilangan1 & bilangan2))
print ('bil1 | bil2 = ', (bilangan1 | bilangan2))
print ('bil1 ^ bil2 = ', (bilangan1 ^ bilangan2))
print ('-' * 80)

print ('bil1 < bil2 = ', (bilangan1 < bilangan2))
print ('bil1 > bil2 = ', (bilangan1 < bilangan2))
print ('bil1 <= bil2 = ', (bilangan1 <= bilangan2))
print ('bil1 >= bil2 = ', (bilangan1 >= bilangan2))
print ('bil1 == bil2 = ', (bilangan1 == bilangan2))
print ('bil1 != bil2 = ', (bilangan1 != bilangan2))

print ('-' * 80)

print ('not True = ', (not True))
print ('True and False = ', (True and False))
print ('True or False = ', (True and False))

total_uang = 10000
harga_barang = 5000
diskon = 0.10

harga_barang *= (1 - diskon)

total_uang -= harga_barang

print ('total uang = %s' % (total_uang))

hasil = 2 + 3 * 4
print ('2 + 3 * 4 = %s' %(hasil))

hasil = (2 + 3) * 4
print ('2 + 3 * 4 = %s' %(hasil))

hasil = 2 / 3 * 4
print ('2 / 3 * 4 = %s' % (hasil))

hasil = 2.0 / 3 * 4
print ('2.0 / 3 * 4 = %s' % (hasil))
