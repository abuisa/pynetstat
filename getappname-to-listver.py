import subprocess
import psutil
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
	
def utama(sf):
	cmd_out = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
	out2list = list(cmd_out)
	out2list = out2list[0].splitlines()

	listku = []
	for row in out2list:
		row2list = row.decode('utf-8').split()
		if row2list: 
			lx = len(row2list)
			if lx == 4: 
				listku += [row2list.insert(3,' - ')]
			listku += [row2list]

	newlistku = [];no = 0	
	newlistku += [["NO","PROTO","LOCAL_IP","FOREIGN_IP","STATE","PID","APP_NAME"]]
	for l in listku:	
		if l:
			if l[0].upper() == 'TCP' or l[0].upper() == 'UDP':
				no +=1; pid = l[-1];exe = get_appname(pid)
				if any(sf.upper() in el.upper() for el in l) or (sf.upper() in exe.upper()) and sf != '':
					l.insert(0,str(no));l.insert(len(l),exe);newlistku += [l]

	ltt = AsciiTable(newlistku);print(ltt.table)

print(ket);print(exp)
while True:
	try:	
		srh = input('\n ENTER, atau masukkan Filter, [x/X for Exit] : ')
		if srh == 'x' or srh == 'X':exit()
		utama(srh)
	except:
		break

