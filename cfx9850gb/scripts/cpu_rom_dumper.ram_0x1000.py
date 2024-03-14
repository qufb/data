#!/usr/bin/env python3

'''
Iterates through 0x100000 bytes at data segment 0, where CPU internal ROM is mapped.
Use a logic analyzer to trace RAM writes.
'''

import sys

with open('cpu.bin', 'wb') as f:
    # Interrupt vector
    b = b'\xff\x88\x00\x30'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\xff' * (0x30 - len(b))

    # Body
    b += b'\xdd\x00\xfc' # ld DS,0x00 ; unk_fc
    b += b'\xff\xff\xff\xff'
    b += b'\x1a\x80\x00' # movq r00,0x00
    #b += b'\x1a\xe0\x00' # movq r60,0x00
    #b += b'\xc1\x60\xfb\xff' # ld#2       r60,0xfb,0xff
    b += b'\xc1\x60\x1d\x18' # ld#2       r60,0x1d,0x18
    # (loop)
    b += b'\x18\x00\x7f' # movb r7f,r00
    for i in range(0x100):
        b += b'\x18\xfe' + bytes([i]) # movb r7e,0x??
        b += b'\x58\x3e\x70'          # movb r70,(r7e)
        #b += b'\xdd\x41\xfc'          # ld DS,0x41 ; unk_fc
        b += b'\xdd\x40\xfc'          # ld DS,0x40 ; unk_fc
        b += b'\x58\x20\xf0'          # movb (r60),r70
        b += b'\xdd\x00\xfc'          # ld DS,0x00 ; unk_fc
    b += b'\x3c\x80\x01' # addb r00,0x01
    b += b'\x14\x80\x00' # cmpb r00,0x00
    b += b'\xa7\x00\x3e' # jmp NZ,0x003e

    b += b'\xff\x88\xf0\x00'
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xff\x88\xf0\x00'

    # ROM check signature
    b += b'\xff' * (0x00fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
