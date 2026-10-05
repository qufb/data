#!/usr/bin/env python3

import sys

with open('cpu.hd620xx.bin', 'wb') as f:
    # 0x0 Interrupt vector
    b = b'\xa7\x00\x30' # jmp &H0030
    b += b'\xc7' * (0x0d - len(b)) # rtn
    b += b'\xff' * (0x20 - len(b)) # rtn
    b += b'\xcf' * (0x30 - len(b)) # rti

    # 0x0030 Setup
    # b += b'\xd6\x00\x20' # ldw v0,&H0020
    # b += b'\xd5\x00\x20' # ldw v1,&H0020
    # b += b'\xd4\x00\x20' # ldw v2,&H0020
    # b += b'\xd3\x00\x20' # ldw v3,&H0020
    b += b'\x88\x00'     # pst ie,&H00 (disable all interrupts)

    b += b'\x89\xfe'     # pst ds,&HFE (RAM on SP and IY, CTRL on IX and IZ)
    b += b'\xd1\x1d\x18' # ldw iy,&H1D18
    b += b'\xd0\xff\xff' # ldw ix,&HFFFF
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80

    b += b'\x89\xfd'     # pst ds,&HFD (RAM on SP and IY, ? on IX and IZ)
    b += b'\xd1\x1d\x18' # ldw iy,&H1D18
    b += b'\xd0\xff\xff' # ldw ix,&HFFFF
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80
    b += b'\x6c\xd0'     # ld r80,(ix)+
    b += b'\x6d\x50'     # st +(iy),r80

    b += b'\x89\xfc'     # pst ds,&HFC (RAM on SP and IY, ROM on IX and IZ)
    b += b'\xd0\x00\x00' # ldw ix,&H0000
    b += b'\x20\xc6\x00' # ld r70,&H00

    # 0x00d2 (loop segment)
    b += b'\x20\x8a\x00' # ld r10,&H00
    b += b'\x20\x8b\x00' # ld r11,&H00

    # 0x00d8 (loop chunk)
    b += b'\x20\x94\x00' # ld r20,&H00
    b += b'\x20\x95\x00' # ld r21,&H00

    # 0x00de (loop 0x100)
    b += b'\x89\xfc'     # pst ds,&HFC (RAM on SP and IY, ROM on IX and IZ)
    b += b'\xd1\x1d\x18' # ldw iy,&H1D18
    b += b'\x6c\xc6'     # ld r70,(ix)+
    b += b'\x6d\x46'     # st +(iy),r70
    b += b'\x6d\x46'     # st +(iy),r70
    b += b'\x6d\x46'     # st +(iy),r70
    b += b'\x6d\x46'     # st +(iy),r70

    # Move to next offset
    b += b'\x0f\x94\x01' # ad r20,&H01
    b += b'\x0b\x14\x00' # tsb r20,&H00
    b += b'\xe3\xde'     # sjmp nz,&H00DE
    # Goto start of loop 0x100 if offset idx < 0x100

    # Move to next chunk
    b += b'\x0f\x8a\x01' # ad r10,&H01
    b += b'\x0b\x0a\x00' # tsb r10,&H00
    b += b'\xe3\xd8'     # sjmp nz,&H00D8
    # Goto start of loop chunk if chunk idx < 0x100

    # Infinite loop (start)
    b += b'\xa7\xf0\x00' # jmp &HF000
    b += b'\xef' * (0x00f000 - len(b))
    b += b'\xa7\xf0\x00'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
