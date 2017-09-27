import subprocess
import sys
cmd = 'netstat -aon'
process = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

while True:
    out = process.stdout.read(1)
    if out == '' and process.poll() != None:
        break
    if out != '':
        ll = out.decode('utf-8')	
        sys.stdout.write(ll)
        sys.stdout.flush()
