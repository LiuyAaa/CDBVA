import os
import time
import re
import sys
import chardet

def main(argv):
   inputfile = ''
start = time.clock()
for num in range(1,10000):
    os.system(sys.argv[1])
end = time.clock()
print('runtime:',end - start)
