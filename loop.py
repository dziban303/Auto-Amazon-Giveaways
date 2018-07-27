from subprocess import Popen
import sys
 
filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
	#change the path to your python installation directory
    p = Popen("python.exe " + filename, shell=True)
    p.wait()
