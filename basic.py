#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp 
import cgi

form = cgi.FieldStorage()

basic = form.getvalue("b")

cmd = sp.getoutput(basic)
print(cmd)
output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]

