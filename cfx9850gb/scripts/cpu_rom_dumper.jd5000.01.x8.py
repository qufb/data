#!/usr/bin/env python3

'''
Iterates through 0x200000 bytes at data segments 0 and 1, where CPU internal ROM is mapped.
Use a logic analyzer to trace RAM writes.
'''

import sys

with open('cpu.jd5000.01.bin', 'wb') as f:
    # 0x0 Interrupt vector
    b = b'\xff\x88\x00\x30'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\x9e\xff\xff\xff'
    b += b'\xff' * (0x30 - len(b))

    # 0x0030 Setup
    b += b'\xc1\x60\x1d\x18' # ld#2 r60,0x1d,0x18
    b += b'\x1a\x80\x00' # movq r00,0x00

    # 0x0037 (loop segment)
    b += b'\x1a\x90\x00' # movq r10,0x00

    # 0x003a (loop chunk)
    b += b'\x18\x10\x7f' # movb r7f,r10
    b += b'\x1a\xa0\x00' # movq r20,0x00

    # 0x0040 (loop 0x100)
    b += b'\x18\x20\x7e' # movb r7e,r20

    b += b'\xdc\x00\xfc' # ld DS,r00 ; unk_fc
    b += b'\x58\x3e\x70' # movb r70,(r7e)
    b += b'\xdd\x40\xfc' # ld DS,0x40 ; unk_fc
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70

    b += b'\xdc\x00\xfc' # ld DS,r00 ; unk_fc
    b += b'\x58\x3e\x70' # movb r70,(r7e)
    b += b'\xdd\x40\xfc' # ld DS,0x40 ; unk_fc
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70
    b += b'\x58\x20\xf0' # movb (r60),r70

    # Move to next offset
    b += b'\x3c\xa0\x01' # addb r20,0x01
    # Goto start of loop 0x100 if offset idx < 0x100
    b += b'\x14\xa0\x00' # cmpb r20,0x00
    b += b'\xa7\x00\x40' # jmp NZ,0x0040

    # Move to next chunk
    b += b'\x3c\x90\x01' # addb r10,0x01
    # Goto start of loop chunk if chunk idx < 0x100
    b += b'\x14\x90\x00' # cmpb r10,0x00
    b += b'\xa7\x00\x3a' # jmp NZ,0x003a

    # Move to next segment
    b += b'\x3c\x80\x01' # addb r00,0x01
    # Goto start of loop segment if segment idx < 0x100
    b += b'\x14\x80\x02' # cmpb r00,0x02
    b += b'\xa7\x00\x37' # jmp NZ,0x0037

    # Infinite loop (start)
    b += b'\xff\x88\xf0\x00'

    # Interrupt vector (power off?)
    b += b'\xff' * (0x000700 - len(b))
    b += b'\xff\x88\x00\x30'
    b += b'\xff' * (0x000710 - len(b))
    b += b'\xff\x88\x00\x30'
    b += b'\xff' * (0x000f00 - len(b))
    b += b'\xff\x88\x00\x30'

    # Infinite loop (continued)
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xff\x88\xf0\x00'

    # ROM check signature
    b += b'\xff' * (0x00fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    b += b'\xff' * (0x01fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
