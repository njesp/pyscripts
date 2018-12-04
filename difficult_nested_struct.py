import binascii

binascii.crc32('Langt filnavn'.encode('utf8'))


a = (1, 2, None, '2018-12-03', 'Lang', None)
c = ['Da', 'Svend Svin', 77, 'DumDummere']
d = {}
d[a] = c
print(d)


print(binascii.crc32('Langt filnavn'.encode('utf8')))
print(binascii.crc32('Langt filnavn2'.encode('utf8')))
