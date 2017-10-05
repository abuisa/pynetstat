import subprocess; import socket
import psutil;import time;import os
from terminaltables import AsciiTable
import getappname_table_output as gto

exp='''-------------------------------------------------
 * Format Output : 
   [1]No. [2]Proto  [3]Local Address  [4]Foreign Address  [5]Host Name [6]State  [7]PID  [8]AppName
-------------------------------------------------
'''

hlp='''
	ENTER, atau masukkan Filter, [x/X for Exit] : 
	R	: Untuk Repeat setiap 2 detik
'''
def get_appname(pid):
	ps = psutil.Process(int(pid))
	return ps.name()
	
def clear_sceen():
    os.system('cls' if os.name == 'nt' else 'clear')
	
def get_dn(ip):
	try:	
		ip = ip.rpartition(':')[0]
		dn = socket.gethostbyaddr(ip)
		dn = dn[0]
		return dn
	except:
		pass
	
def utama(sf):
	cmd_out = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
	out2list = list(cmd_out)
	out2list = out2list[0].splitlines()

	#clear_sceen()
	listku = []
	for row in out2list:
		row2list = row.decode('utf-8').split()
		if row2list: 
			lx = len(row2list)
			if lx == 4: 
				listku += [row2list.insert(3,' - ')]
			listku += [row2list]

	newlistku = [];no = 0	
	newlistku += [["NO","PROTO","LOCAL_IP","FOREIGN_IP","HOST_NAME","STATE","PID","APP_NAME"]]
	for l in listku:	
		if l:
			if l[0].upper() == 'TCP' or l[0].upper() == 'UDP':
				pid = l[-1];exe = get_appname(pid)
				if any(sf.upper() in el.upper() for el in l) or (sf.upper() in exe.upper()) and sf != '':
					no +=1;l.insert(0,str(no));l.insert(4,get_dn(l[3]));l.insert(len(l),exe);newlistku += [l]

	ltt = AsciiTable(newlistku);print(ltt.table) 

def main():
	print(gto.ket);print(exp)
	while True:
		try:	
			srh = input('\n ENTER, atau masukkan Filter, [x/X for Exit] : ')
			if srh == 'x' or srh == 'X':exit()			
			if srh == 'H' or srh == 'h':
				print(hlp)
			if srh == 'R':
				srh = input('\n Repeat untuk Filter, [x/X for Exit] : ')
				while True:				
					utama(srh)
					print(exp)
					time.sleep(2)	
			utama(srh)
		except:
			break

#main()
