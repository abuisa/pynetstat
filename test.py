import getappname_table_output as gto
import getappname_to_listver as gtl


ket = '''***************************************************************
Silahkan Pilih : 
 1. Tampilan output akan seperti : 
'''+gto.exp+'''
 2. Tampilan output akan seperti : 
'''+gtl.exp+'''
***************************************************************
'''


print(ket)
pilih = input(' Pilih No : ')
if pilih == '1':
	gto.main()
elif pilih == '2':
	gtl.main()
else:
	print('Maaf !, Pilihan Tidak Tersedia..!')