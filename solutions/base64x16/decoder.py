#!/usr/bin/env python2.7

import base64

data = ''
with open('encoded.txt', 'r') as f:
    data = f.read()

for i in range(0, 16):
    data = base64.b64decode(data)

arr = data.split("TDOH")

for a in arr:
    print("TDOH%s" % (a, ))
