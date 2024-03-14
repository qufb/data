#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'rb') as f:
    rom = f.read()

with open('test.bin', 'wb') as f:
    f.write(rom)

    # zero contrast (OPT = 0)
    #f.seek(0x4c)
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')

    # pixels fill entire rows
    #f.seek(0x143)
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')
    #f.write(b'\xff\xff\xff')

    #required for display to turn on...
    #f.seek(0x169)
    #f.write(b'\xff\xff\xff')

    #f.seek(0x58) # nok
    f.seek(0x64) # ok
    #f.seek(0x331) # ok
    f.write(b'\xff\x88\xd0\x00\xff\xff')
    f.seek(0xd000)

    f.write(b'\xb1\xb9') #             port_ctrl  0xb9
    f.write(b'\xe6\x7e') #             ld         R7E,PORT
    f.write(b'\x2c\xfe\x4f') #         and#0x1    R7E,0x4f
    f.write(b'\xc1\x40\x00\x00') #     ld#2       R40,0x0,0x0
    f.write(b'\x58\x00\xfe') #         ld#0x1     (R40),R7E
    f.write(b'\xf2\x7e') #             out        PORT,R7E
    f.write(b'\xfc') #                 unk_fc
    f.write(b'\x18\xc2\xff') #         ld#0x1     R42,0xff
    f.write(b'\xdd\x40') #             ld         DS,0x40
    f.write(b'\xc1\x40\x00\xf8') #     ld#2       R40,0x0,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x01\xf8') #     ld#2       R40,0x1,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x02\xf8') #     ld#2       R40,0x2,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x03\xf8') #     ld#2       R40,0x3,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x04\xfc') #     ld#2       R40,0x4,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x05\xfc') #     ld#2       R40,0x5,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x06\xfc') #     ld#2       R40,0x6,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x07\xfc') #     ld#2       R40,0x7,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xdd\x60') #             ld         DS,0x60
    f.write(b'\xc1\x40\x10\xf8') #     ld#2       R40,0x10,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x11\xf8') #     ld#2       R40,0x11,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x12\xf8') #     ld#2       R40,0x12,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x13\xf8') #     ld#2       R40,0x13,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x14\xfc') #     ld#2       R40,0x14,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x15\xfc') #     ld#2       R40,0x15,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x16\xfc') #     ld#2       R40,0x16,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x17\xfc') #     ld#2       R40,0x17,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xdd\x40') #             ld         DS,0x40
    f.write(b'\xc1\x40\x20\xf8') #     ld#2       R40,0x20,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x21\xf8') #     ld#2       R40,0x21,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x22\xf8') #     ld#2       R40,0x22,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x23\xf8') #     ld#2       R40,0x23,0xf8
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x24\xfc') #     ld#2       R40,0x24,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x25\xfc') #     ld#2       R40,0x25,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x26\xfc') #     ld#2       R40,0x26,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x27\xfc') #     ld#2       R40,0x27,0xfc
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xdd\x40') #             ld         DS,0x40
    f.write(b'\xc1\x40\x30\xf0') #     ld#2       R40,0x30,0xf0
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x31\xf0') #     ld#2       R40,0x31,0xf0
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x32\xf0') #     ld#2       R40,0x32,0xf0
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x33\xf0') #     ld#2       R40,0x33,0xf0
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x34\xf4') #     ld#2       R40,0x34,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x35\xf4') #     ld#2       R40,0x35,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x36\xf4') #     ld#2       R40,0x36,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x37\xf4') #     ld#2       R40,0x37,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x38\xf4') #     ld#2       R40,0x38,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x39\xf4') #     ld#2       R40,0x39,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x3a\xf4') #     ld#2       R40,0x3a,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42
    f.write(b'\xc1\x40\x3b\xf4') #     ld#2       R40,0x3b,0xf4
    f.write(b'\x58\x00\xc2') #         ld#0x1     (R40),R42

    f.write(b'\x1b\xe0\x00')     # ld#0x8     R60,0x00
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xfc') #          ?

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xfd') #          ?

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xf1\x00') #          ?

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x08') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xf3\x00') #          ?

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xb9\x00') #          unk_b9     0x8
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    f.write(b'\xb3\x07') #          timer_set  0x07
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xfe') #              timer_wait
    f.write(b'\xb3\x49') #          timer_set  0x49
    f.write(b'\xfe') #              timer_wait

    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60

    # Infinite loop
    f.write(b'\xff\x88\xe0\x00')
    f.write(b'\xff' * (0x00e000 - f.tell()))
    f.write(b'\xb3\x49')         # timer_set  0x49  # 837.61ms
    f.write(b'\xb9\x08')
    f.write(b'\xfe')             # timer_wait
    f.write(b'\xe5\x60')         # ld#0x1     R60,TIME
    f.write(b'\x5b\x10\xe0')     # ld#0x8     (R50),R60
    f.write(b'\x88\xe0\x00')
