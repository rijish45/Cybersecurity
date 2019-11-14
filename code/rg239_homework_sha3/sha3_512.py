#Library used - https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

import sys
from Crypto.Hash import SHA3_512

if (len(sys.argv) < 2):
    exit(1)
else:
    filename = sys.argv[1]
    with open(filename, 'r') as myfile:
        data = myfile.read()
    #print(data)
    h_obj = SHA3_512.new()
    h_obj.update(data)
    print(h_obj.hexdigest())
    exit(0)
