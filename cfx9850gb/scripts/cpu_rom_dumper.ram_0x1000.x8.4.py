#!/usr/bin/env python3

'''
Iterates through 0x100000 bytes at data segment 0, where CPU internal ROM is mapped.
Use a logic analyzer to trace RAM writes.
'''

import sys

with open('cpu.bin', 'wb') as f:
    # Blank
    b = b'\xff' * 0x100000

    f.write(b)

    f.seek(0)

    b = b''

    # Interrupt vector
    b += b'\xff\x88\x00\x30'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\xff' * (0x30 - len(b))

    # Body
    ## ld#0x1 R39,0x0
    #b += b'\x18\xb9\x00'
    ## ld#0x1 R3A,0x0
    #b += b'\x18\xba\x00'
    ## ld#0x1 R3B,0x40
    #b += b'\x18\xbb\x40'
    ## ld#0x1 R3C,0x1
    #b += b'\x18\xbc\x01'
    ## ld#0x1 R3D,0x0
    #b += b'\x18\xbd\x00'
    ## ld#0x1 R3E,0xa0
    #b += b'\x18\xbe\xa0'
    ## out KOL,R3D
    #b += b'\xb6\x3d'
    ## out KOH,R3E
    #b += b'\xb4\x3e'
    ## port_ctrl 0x7f
    #b += b'\xb1\x7f'
    ## out PORT,R3B
    #b += b'\xf2\x3b'
    ## out 0x6,R3C
    #b += b'\xf6\x3c'
    ## out OPT,0xc0
    #b += b'\xf1\xc0'

    # unk_fc
    b += b'\xfc'

    # ld#2 R70,0xfa,0x2
    b += b'\xc1\x70\xfa\x02'
    # ld DS,0x8
    b += b'\xd5\x08'
    # ld#2 (R70),0
    b += b'\x59\xb0\x00'
    # ld#2 R70,0xf8,0x2
    b += b'\xc1\x70\xf8\x02'
    # ld SS,0x8
    b += b'\xd5\x08'
    # ld SP,R70
    b += b'\xd6\x70'

    # ld DS,0x40
    b += b'\xdd\x40'
    # ld DSIZE,0xf7
    b += b'\xd3\xf7'

    ## unk_b9 0x0
    #b += b'\xb9\x00'
    ## unk_f5 0x0
    #b += b'\xf5\x00'

    # ld#2 R78,0x40,0x18
    b += b'\xc1\x78\x40\x18'
    # ld#2 R7A,(R78)
    b += b'\x59\x38\x7a'
    # cmp#2 R7A,0x77
    b += b'\x15\xfa\x77'
    # jmp Z ,0x0075
    b += b'\xa3\x00\x75'
    # ld#1 (R78),0x77
    b += b'\x58\xf8\x77'

    # ld#2 R78,0x44,0x18
    b += b'\xc1\x78\x44\x18'
    # ld#1 (R78),0x00
    b += b'\x58\xf8\x00'

    b += b'\xff\xff\xff\xff'
    b += b'\x1a\x80\x00' # movq r00,0x00

    # (loop)
    b += b'\x18\x00\x7f' # movb r7f,r00

    # ld#2 R78,0x44,0x18
    b += b'\xc1\x78\x44\x18'
    # ld#1 R7E,(R78)
    b += b'\x58\x38\x7e'

    # ld LAR,R7E
    b += b'\xde\x7e'
    # ld DS,0
    b += b'\xdd\x00'
    # jmp 0x8000
    b += b'\x88\x80\x00'
    # ld DS,0x40
    b += b'\xdd\x40'
    # ld#2 R60,0x1d,0x18
    b += b'\xc1\x60\x1d\x18'
    b += b'\x58\x20\x90' # ld#1 (R60),R10
    b += b'\x58\x20\x90' # ld#1 (R60),R10
    b += b'\x58\x20\x90' # ld#1 (R60),R10
    b += b'\x58\x20\x90' # ld#1 (R60),R10
    b += b'\x58\x20\x91' # ld#1 (R60),R11
    b += b'\x58\x20\x91' # ld#1 (R60),R11
    b += b'\x58\x20\x91' # ld#1 (R60),R11
    b += b'\x58\x20\x91' # ld#1 (R60),R11
    b += b'\x58\x20\x92' # ld#1 (R60),R12
    b += b'\x58\x20\x92' # ld#1 (R60),R12
    b += b'\x58\x20\x92' # ld#1 (R60),R12
    b += b'\x58\x20\x92' # ld#1 (R60),R12
    b += b'\x58\x20\x93' # ld#1 (R60),R13
    b += b'\x58\x20\x93' # ld#1 (R60),R13
    b += b'\x58\x20\x93' # ld#1 (R60),R13
    b += b'\x58\x20\x93' # ld#1 (R60),R13
    b += b'\x58\x20\x94' # ld#1 (R60),R14
    b += b'\x58\x20\x94' # ld#1 (R60),R14
    b += b'\x58\x20\x94' # ld#1 (R60),R14
    b += b'\x58\x20\x94' # ld#1 (R60),R14
    b += b'\x58\x20\x95' # ld#1 (R60),R15
    b += b'\x58\x20\x95' # ld#1 (R60),R15
    b += b'\x58\x20\x95' # ld#1 (R60),R15
    b += b'\x58\x20\x95' # ld#1 (R60),R15
    b += b'\x58\x20\x96' # ld#1 (R60),R16
    b += b'\x58\x20\x96' # ld#1 (R60),R16
    b += b'\x58\x20\x96' # ld#1 (R60),R16
    b += b'\x58\x20\x96' # ld#1 (R60),R16
    b += b'\x58\x20\x97' # ld#1 (R60),R17
    b += b'\x58\x20\x97' # ld#1 (R60),R17
    b += b'\x58\x20\x97' # ld#1 (R60),R17
    b += b'\x58\x20\x97' # ld#1 (R60),R17
    b += b'\x58\x20\x98' # ld#1 (R60),R18
    b += b'\x58\x20\x98' # ld#1 (R60),R18
    b += b'\x58\x20\x98' # ld#1 (R60),R18
    b += b'\x58\x20\x98' # ld#1 (R60),R18
    b += b'\x58\x20\x99' # ld#1 (R60),R19
    b += b'\x58\x20\x99' # ld#1 (R60),R19
    b += b'\x58\x20\x99' # ld#1 (R60),R19
    b += b'\x58\x20\x99' # ld#1 (R60),R19
    b += b'\x58\x20\x9a' # ld#1 (R60),R1a
    b += b'\x58\x20\x9a' # ld#1 (R60),R1a
    b += b'\x58\x20\x9a' # ld#1 (R60),R1a
    b += b'\x58\x20\x9a' # ld#1 (R60),R1a
    b += b'\x58\x20\x9b' # ld#1 (R60),R1b
    b += b'\x58\x20\x9b' # ld#1 (R60),R1b
    b += b'\x58\x20\x9b' # ld#1 (R60),R1b
    b += b'\x58\x20\x9b' # ld#1 (R60),R1b
    b += b'\x58\x20\x9c' # ld#1 (R60),R1c
    b += b'\x58\x20\x9c' # ld#1 (R60),R1c
    b += b'\x58\x20\x9c' # ld#1 (R60),R1c
    b += b'\x58\x20\x9c' # ld#1 (R60),R1c
    b += b'\x58\x20\x9d' # ld#1 (R60),R1d
    b += b'\x58\x20\x9d' # ld#1 (R60),R1d
    b += b'\x58\x20\x9d' # ld#1 (R60),R1d
    b += b'\x58\x20\x9d' # ld#1 (R60),R1d
    b += b'\x58\x20\x9e' # ld#1 (R60),R1e
    b += b'\x58\x20\x9e' # ld#1 (R60),R1e
    b += b'\x58\x20\x9e' # ld#1 (R60),R1e
    b += b'\x58\x20\x9e' # ld#1 (R60),R1e
    b += b'\x58\x20\x9f' # ld#1 (R60),R1f
    b += b'\x58\x20\x9f' # ld#1 (R60),R1f
    b += b'\x58\x20\x9f' # ld#1 (R60),R1f
    b += b'\x58\x20\x9f' # ld#1 (R60),R1f
    # unk_fc
    b += b'\xfc'

    # ld#2 R78,0x44,0x18
    b += b'\xc1\x78\x44\x18'
    # ld#1 R7E,(R78)
    b += b'\x58\x38\x7e'
    # add#1 R7E,0x10
    b += b'\x3c\xfe\x10'
    # ld#1 (R78),R7E
    b += b'\x58\x38\xfe'
    # cmp#1 R7E,0
    b += b'\x14\xfe\x00'
    # jmp NZ,0x64
    b += b'\xa7\x00\x64'

    b += b'\x3c\x80\x01' # addb r00,0x01
    b += b'\x14\x80\x00' # cmpb r00,0x00
    b += b'\xa7\x00\x64' # jmp NZ,0x0064

    b += b'\xff\x88\xf0\x00'
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xff\x88\xf0\x00'

    f.write(b)

    f.seek(0x8000)

    b = b''
    # jmpf 0x0014c8
    b += b'\x89\x00\x14\xc8'

    f.write(b)

    f.seek(0xfff0)

    # ROM check signature
    b = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    f.write(b)
