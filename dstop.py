#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

osstop = form.getvalue("s")

cmd = "sudo docker stop {}".format(osstop)

output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status == 0:
    print("Your OS {} has been Stoped Successfully".format(osstop))
else:
    print("{}".format(out))

    

