from subprocess import Popen
import sys
 
filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
    p = Popen("f:\python36\python.exe " + filename, shell=True)
    p.wait()