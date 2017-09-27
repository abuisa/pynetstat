import subprocess
import psutil
import csv


def get_process(pid):
	ps = psutil.Process(int(pid))
	return ps.name()
	
def write_2log(fl,s):
	try:
		f = open(fl,'w')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
		f.close
		
cmd_out = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
out_tolist = list(cmd_out)

for out_line in out_tolist:
	if out_line != None:
		out_line = out_line.decode('utf-8') 
		write_2log('NetStat.out',out_line)

	
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
					exe = get_process(pid)
					p_out = str(ix)+'.'+s+ pro +s+ sta +s+loa +s+s+  foa +s+ pid +s+ exe
					print (p_out)
				except Exception as e:
					print (e)
				#print('-------------------------------------------------')

def output_v2():
	f = open("NetStat.out")
	csv_f = csv.reader(f)
	for row in csv_f:
		if row:
			row_tol = row[0].split()
			pro = row_tol[0]
			pid = row_tol[-1]
			if pro == "TCP" or pro == "UDP":		
				exe = get_process(pid)
				#print(exe)
				#print(pro +'\t'+pid)
				row = row[0]
				print(row + '\t' +exe)

				
				
#output_v1()
print ('====================================================')
output_v2()