file_list = ["1.pdf", "2.pdf", "3.pdf"]

apps = [
    "epdfview",
    "acroread"
    ]

fuzz_output = "fuzz.pdf"

FuzzFactor = 100
num_tests = 100

import math
import random
import string
import subprocess
import time

def rand_fuzzer(buf, numwrites):    
    for j in range(numwrites):
        rbyte= random.randrange(256)
        rn=random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte);
        
for i in xrange(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)
    buf = bytearray(open(file_choice, 'rb').read())

    # start Charlie Miller code (modified)
    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
    rand_fuzzer(buf, numwrites)
    # end Charlie Miller code (modified)

    open(fuzz_output, 'wb').write(buf)

    print "Using app: %s orig_file: %s #writes=%d" % (app, file_choice, numwrites)
    process = subprocess.Popen([app, fuzz_output])
    
    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()
    else:
        print "Crashed"
