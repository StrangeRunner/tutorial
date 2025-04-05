#!/bin/python
from __future__ import print_function
import sys
import re
import os.path

if len(sys.argv) > 1:
    f_in = open(sys.argv[1],'r')
#    root,ext = os.path.splitext(sys.argv[1])
else:
    print ('Usage:%s finename' % sys.argv[0])
    sys.exit()

for ele in f_in:
#    ele = ele.rstrip(r'\n')
#    ele = ele.rstrip('\n')
#    ele1 = re.split(r'\s+',ele)
    print(ele,end="")

f_in.close()
