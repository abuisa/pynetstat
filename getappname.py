import subprocess
import psutil
import csv

ket= '''-------------------------------------------------
 * netstat untuk menampilkan applikasi yang sedang menggunakan port
 * hasilnya sama dengan <netstat -ab> tapi beda format output dan tidak ada waktu tunggu
 * output bisa difilter 
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
		out_line = out_line.decode('utf-8') 
		w2file('NetStat.out',out_line)

	
def output_v1():
	tmp_file = [i.strip().split() for i in open("NetStat.out")]
	ix = 0
	for f_line in tmp_file:
		if f_line :
			if f_line[0] == "TCP" or f_line[0] == "UDP":
				ix = ix+1
				try:
					jum = len(f_line)	
					s = '\t'
					pro = f_line[0]
					loa = f_line[1]
					foa = f_line[2]
					if jum == 5: sta = f_line[3]
					else: sta = '\t\t'
					pid = f_line[-1]
					exe = get_appname(pid)
					p_out = str(ix)+'.'+s+ pro +s+ sta +s+loa +s+s+  foa +s+ pid +s+ exe
					#p_out = '\t'.join(f_line)
					print (p_out)
				except Exception as e:
					print (e)
				

				
def output_v2(str_filter):
	no = 0
	f = open("NetStat.out")
	csv_f = csv.reader(f)
	#hdr_s = ["NO","PROTO","LOCAL_IP","FOREIGN_IP","STATE","PID","APP_NAME"]
	#print ('\t'.join(hdr_s))
	for row in csv_f:
		if row:
			row_tol = row[0].split()
			pro = row_tol[0]
			pid = row_tol[-1]
			if pro == "TCP" or pro == "UDP":
				exe = get_appname(pid)
				row = row[0]				
				if any(str_filter.upper() in el_row.upper() for el_row in row_tol) or (str_filter.upper() in exe.upper())  and str_filter != '':
					no = no + 1					
					print(' '+str(no)+'.\t'+ row + '\t' +exe)
				elif str_filter == '':
					no = no + 1
					print(' '+str(no)+'.\t'+ row + '\t' +exe)				
				#else:
				#	print(' Filter Not Found !')



while True:
	try:	
		print(ket) # beri tanda pagar jika tidak ingin tampilkan baris ini 
		str_filter = input('\n Masukkan String untuk Filter output, [x/X for Exit] : ')
		print('------------------------------------------------------------')
		if str_filter == 'x' or str_filter == 'X':
			exit()
		#output_v1()
		output_v2(str_filter)	
	except:
		break
