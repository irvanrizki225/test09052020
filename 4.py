import re
kata = input("masukan kata :")
hasil = len(re.findall(r'r', kata))
print ('Ditemukan '+ hasil +' kata')
