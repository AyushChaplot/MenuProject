#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

rmos = form.getvalue("r")

cmd = "sudo docker rm {}".format(rmos)

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
    print("os {} has been removed Sucessfully..".format(rmos))
else:
    print("{}".format(out))

