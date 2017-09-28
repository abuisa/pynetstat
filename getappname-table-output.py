import subprocess
import psutil
import csv
from terminaltables import AsciiTable

ket= '''-------------------------------------------------
 * netstat untuk menampilkan applikasi yang sedang menggunakan port
 * hasilnya sama dengan <netstat -ab> tapi beda format output dan tidak ada waktu tunggu
 * output bisa difilter 

 * Contoh 1 Filter, menampilkan yang mengandung kata 'firefox': 
   ENTER !, atau masukkan Filter [x/X for Exit] : firefox 
 * Contoh 2 Filter, menampilkan yang mengandung kata 'UDP': 
   ENTER !, atau masukkan Filter [x/X for Exit] : udp 
-------------------------------------------------
'''
exp='''-------------------------------------------------
 * Format Output : 
   [1]No. [2]Proto  [3]Local Address  [4]Foreign Address  [5]State  [6]PID  [7]AppName
-------------------------------------------------
'''


def get_appname(pid):
	ps = psutil.Process(int(pid))
	return ps.name()
	
def w2file(fl,s):
	try:
		f = open(fl,'w')
		f.write(s+"\n")
	except:
		exit()
	f.close

cmd_out = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
out_tolist = list(cmd_out)

for out_line in out_tolist:
	if out_line != None:
		out_line = out_line.decode('utf-8') # decode, untuk python 3
		w2file('NetStat.out',out_line)



def output_2tabel(sf):
	no = 0
	frow =[]
	hdr_s = ["NO","PROTO","LOCAL_IP","FOREIGN_IP","STATE","PID","APP_NAME"]
	frow += [hdr_s]
	of = [i.strip().split() for i in open("NetStat.out")]	
	for row in of:
		if row:			
			if row[0].upper() == 'TCP' or row[0].upper() == 'UDP':	
				pid = row[-1]			
				exe = get_appname(pid)
				if any(sf.upper() in el.upper() for el in row) or (sf.upper() in exe.upper()) and sf != '':
					no = no+1
					row.insert(0,str(no))
					jum = len(row)
					if jum == 5: row.insert(4,' - ')
					row.insert(6,exe)
					frow += [row]

	ltt = AsciiTable(frow)
	print(ltt.table)



		
#output_2tabel()

print(ket)
print(exp)
while True:
	try:	
		str_filter = input('\n ENTER, atau masukkan Filter, [x/X for Exit] : ')
		if str_filter == 'x' or str_filter == 'X':
			exit()
		output_2tabel(str_filter)
	except:
		break
