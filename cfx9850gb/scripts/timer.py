#!/usr/bin/env python3

import sys

with open('./r27v802d-34.lsi2', 'rb') as f:
    rom = f.read()

with open('timer.bin', 'wb') as f:
    f.write(rom)

    f.seek(0x152)
    f.write(b'\xff\x88\xd0\x00\xff\xff')
    f.seek(0xd000)

    f.write(b'\xf7\xc0')
    f.write(b'\xb3\x07\xb9\x00\xfe')
    f.write(b'\xb3\x07\xb9\x02\xfe')
    f.write(b'\xb3\x07\xb9\x22\xfe')

    f.write(b'\xf7\x80')
    f.write(b'\xb3\x07\xb9\x00\xfe')
    f.write(b'\xb3\x07\xb9\x02\xfe')
    f.write(b'\xb3\x07\xb9\x22\xfe')

    f.write(b'\xf7\x40')
    f.write(b'\xb3\x07\xb9\x00\xfe')
    f.write(b'\xb3\x07\xb9\x02\xfe')
    f.write(b'\xb3\x07\xb9\x22\xfe')

    f.write(b'\xf7\x00')
    f.write(b'\xb3\x07\xb9\x00\xfe')
    f.write(b'\xb3\x07\xb9\x02\xfe')
    f.write(b'\xb3\x07\xb9\x22\xfe')

    f.write(b'\xff\x88\xe0\x00')
    f.write(b'\xff' * (0x00e000 - f.tell()))
    f.write(b'\xff\x88\xe0\x00\xff\xff\xff\xff')
