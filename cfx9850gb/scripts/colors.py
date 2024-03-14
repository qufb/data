#!/usr/bin/env python3

import sys

with open('test.bin', 'wb') as f:
    # Interrupt vector
    b = b'\xff\x88\x00\x30'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\xff' * (0x30 - len(b))

    # Init
    b += b'\xf1\x00\xb5\x80\xb7\x00\xb1\xff\xf3\x00\xdd\x40\xfc\xc1\x70\xff\x02\xd5\x08\xd6\x70\xb3\x03\xb9\x00\xf5\x00\xff'

    b += b'\x8e'              # unk_8e
    b += b'\x18\xfc\x07'      # ld#0x1     R7C,0x07
    b += b'\xe1\x7d'          # in         R7D,OPT
    b += b'\x2c\xfd\xf0'      # and#0x1    R7D,0xf0
    b += b'\x2c\xfc\x0f'      # and#0x1    R7C,0xf
    b += b'\x24\x7c\x7d'      # or#0x1     R7C,R7D
    b += b'\xf0\x7d'          # out        OPT,R7D

    b += b'\xb1\xb9'         # unk_b1 0xb9
    b += b'\xe6\x7e'         # in         R7E,PORT
    b += b'\x2c\xfe\x4f'     # and#0x1    R7E,0x4f
    #b += b'\xc1\x40\x00\x00' # ld2        R40,0x0000
    #b += b'\x58\x00\xfe'     # ld1        (R40),R7E => 04
    #b += b'\x24\xfe\x01'     # or#0x1     R7E,0x01
    b += b'\xf2\x7e'         # out        PORT,R7E
    b += b'\xfc'             # unk_fc

    b += b'\xff\xff\xff\xff'

    b += b'\x18\xc2\xff'     # ld1 r42,0xff

    b += b'\xdd\x40'         # ld  DS,0x40
    b += b'\xc1\x40\x00\xf8' # ld2 r40,0xf800
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x01\xf8' # ld2 r40,0xf801
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x02\xf8' # ld2 r40,0xf802
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x03\xf8' # ld2 r40,0xf803
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x04\xfc' # ld2 r40,0xfc04
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x05\xfc' # ld2 r40,0xfc05
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x06\xfc' # ld2 r40,0xfc06
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x07\xfc' # ld2 r40,0xfc07
    b += b'\x58\x00\xc2'     # ld1 (r40),r42

    b += b'\xdd\x60'         # ld  DS,0x60
    b += b'\xc1\x40\x10\xf8' # ld2 r40,0xf810
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x11\xf8' # ld2 r40,0xf811
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x12\xf8' # ld2 r40,0xf812
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x13\xf8' # ld2 r40,0xf813
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x14\xfc' # ld2 r40,0xfc14
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x15\xfc' # ld2 r40,0xfc15
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x16\xfc' # ld2 r40,0xfc16
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x17\xfc' # ld2 r40,0xfc17
    b += b'\x58\x00\xc2'     # ld1 (r40),r42

    b += b'\xdd\x40'         # ld  DS,0x40
    b += b'\xc1\x40\x20\xf8' # ld2 r40,0xf820
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x21\xf8' # ld2 r40,0xf821
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x22\xf8' # ld2 r40,0xf822
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x23\xf8' # ld2 r40,0xf823
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x24\xfc' # ld2 r40,0xfc24
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x25\xfc' # ld2 r40,0xfc25
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x26\xfc' # ld2 r40,0xfc26
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x27\xfc' # ld2 r40,0xfc27
    b += b'\x58\x00\xc2'     # ld1 (r40),r42

    b += b'\xdd\x40'         # ld  DS,0x40
    b += b'\xc1\x40\x30\xc8' # ld2 r40,0xc830
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x31\xc8' # ld2 r40,0xc831
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x32\xc8' # ld2 r40,0xc832
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x33\xc8' # ld2 r40,0xc833
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x34\xcc' # ld2 r40,0xcc34
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x35\xcc' # ld2 r40,0xcc35
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x36\xcc' # ld2 r40,0xcc36
    b += b'\x58\x00\xc2'     # ld1 (r40),r42
    b += b'\xc1\x40\x37\xcc' # ld2 r40,0xcc37
    b += b'\x58\x00\xc2'     # ld1 (r40),r42

    b += b'\xff\x88\xf0\x00'
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xff\x88\xf0\x00'

    # ROM check signature
    b += b'\xff' * (0x00fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
