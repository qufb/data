#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'rb') as f:
    rom = f.read()

with open('timer.break.bin', 'wb') as f:
    f.write(rom)

    #f.seek(0x152)
    #f.seek(0x331)
    f.seek(0xe94)
    f.write(b'\xff\x88\xd0\x00\xff\xff')
    f.seek(0xd000)

    f.write(b'\xf7\xc0')
    f.write(b'\xb3\x49\xb9\x08\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe')

    f.write(b'\xff\xff\xff\xff')
    f.write(b'\xff\xff\xff\xff')

    f.write(b'\xb3\x07\xb9\x08\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe')

    f.write(b'\xff\x88\xe0\x00')
    f.write(b'\xff' * (0x00e000 - f.tell()))
    f.write(b'\xff\x88\xe0\x00\xff\xff\xff\xff')
