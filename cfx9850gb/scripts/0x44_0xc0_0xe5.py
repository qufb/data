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

    # init
    b += b'\xd3\x37'         # ld         DSIZE,0x37
    b += b'\xdd\x40'         # ld         DS,0x40

    # sanity check
    b += b'\xd9\x03'         # ld         F,0x03
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\xd9\x13'         # ld         F,0x13
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\xd9\x33'         # ld         F,0x33
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\xd9\x3f'         # ld         F,0x3f
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    # 0x44..0x47
    b += b'\xc1\x40\x10\x10' # ld#2       R40,0x10,0x10
    b += b'\xc1\x50\x20\x20' # ld#2       R50,0x20,0x20
    b += b'\xc1\x10\x0f\x0f' # ld#2       R10,0x0f,0x0f
    b += b'\xc1\x20\x0f\x00' # ld#2       R20,0x0f,0x00
    b += b'\x59\x00\x90'     # ld#0x2     (R40),R10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
    
    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
   
    b += b'\xc1\x40\x10\x10' # ld#2       R40,0x10,0x10
    b += b'\xc1\x50\x20\x20' # ld#2       R50,0x20,0x20
    b += b'\xc1\x10\xf0\xf0' # ld#2       R10,0xf0,0xf0
    b += b'\xc1\x20\xf0\x00' # ld#2       R20,0xf0,0x00
    b += b'\x59\x00\x90'     # ld#0x2     (R40),R10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
    
    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
   
    b += b'\xc1\x40\x10\x10' # ld#2       R40,0x10,0x10
    b += b'\xc1\x50\x20\x20' # ld#2       R50,0x20,0x20
    b += b'\xc1\x10\x00\x00' # ld#2       R10,0x00,0x00
    b += b'\xc1\x20\xf0\x00' # ld#2       R20,0xf0,0x00
    b += b'\x59\x00\x90'     # ld#0x2     (R40),R10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
    
    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x44\x00\xa0'     # msk#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42
   
    b += b'\xc1\x40\x10\x10' # ld#2       R40,0x10,0x10
    b += b'\xc1\x50\x20\x20' # ld#2       R50,0x20,0x20
    b += b'\xc1\x10\x0f\x0f' # ld#2       R10,0x0f,0x0f
    b += b'\xc1\x20\x0f\x00' # ld#2       R20,0x0f,0x00
    b += b'\x59\x00\x90'     # ld#0x2     (R40),R10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x45\x00\xa0'     # msk#0x2    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x45\x00\xa0'     # msk#0x2    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xc1\x20\x0f\x0f' # ld#2       R20,0x0f,0x0f
    b += b'\xc1\x22\x00\x0f' # ld#2       R22,0x00,0x0f
    b += b'\xc1\x24\x0f\x0f' # ld#2       R24,0x0f,0x0f
    b += b'\xc1\x26\x0f\x0f' # ld#2       R26,0x0f,0x0f
   
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    b += b'\xd3\x11'         # ld         DSIZE,0x11

    b += b'\xc1\x20\x0f\x0f' # ld#2       R20,0x0f,0x0f
    b += b'\xc1\x22\x0f\x0f' # ld#2       R22,0x0f,0x0f
    b += b'\xc1\x24\x0f\x0f' # ld#2       R24,0x0f,0x0f
    b += b'\xc1\x26\x00\x0f' # ld#2       R26,0x00,0x0f
   
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    b += b'\xd3\xff'         # ld         DSIZE,0xff

    b += b'\xc1\x20\x0f\x0f' # ld#2       R20,0x0f,0x0f
    b += b'\xc1\x22\x0f\x0f' # ld#2       R22,0x0f,0x0f
    b += b'\xc1\x24\x0f\x0f' # ld#2       R24,0x0f,0x0f
    b += b'\xc1\x26\x00\x0f' # ld#2       R26,0x00,0x0f
   
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x46\x00\xa0'     # msk#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F

    # 0xc0..0xc3
    b += b'\xd3\x37'         # ld         DSIZE,0x37
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc0\x20\x10\xff' # ld#1       R20,0x10
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc1\x20\x11\xff' # ld#2       R20,0x11,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc2\x20\x12\x0f' # ld#4       R20,0x12,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc3\x20\x13\xff' # ld#8       R20,0x13,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xd3\xff'         # ld         DSIZE,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc0\x20\x10\xff' # ld#1       R20,0x10
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc1\x20\x11\xff' # ld#2       R20,0x11,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc2\x20\x12\x0f' # ld#4       R20,0x12,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc3\x20\x13\xff' # ld#8       R20,0x13,...
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20

    # swp
    b += b'\xd3\x37'         # ld         DSIZE,0x37

    b += b'\xc1\x20\x00\x00' # ld#2       R20,0x00,0x00
    b += b'\xc1\x22\x00\x00' # ld#2       R22,0x00,0x00
    b += b'\xc1\x24\x00\x00' # ld#2       R24,0x00,0x00
    b += b'\xc1\x26\x00\x00' # ld#2       R26,0x00,0x00
    b += b'\xc1\x28\x00\x00' # ld#2       R28,0x00,0x00
    b += b'\xc1\x2a\x00\x00' # ld#2       R2A,0x00,0x00
    b += b'\xc1\x2c\x00\x00' # ld#2       R2C,0x00,0x00
    b += b'\xc1\x2e\x00\x10' # ld#2       R2E,0x00,0x00

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcc\x00\xa1'     # swp#0x1    (R40),R21
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xc1\x20\x00\x00' # ld#2       R20,0x00,0x00
    b += b'\xc1\x22\x00\x00' # ld#2       R22,0x00,0x00
    b += b'\xc1\x24\x00\x00' # ld#2       R24,0x00,0x00
    b += b'\xc1\x26\x00\x00' # ld#2       R26,0x00,0x00
    b += b'\xc1\x28\x00\x00' # ld#2       R28,0x00,0x00
    b += b'\xc1\x2a\x00\x00' # ld#2       R2A,0x00,0x00
    b += b'\xc1\x2c\x00\x00' # ld#2       R2C,0x00,0x00
    b += b'\xc1\x2e\x00\x10' # ld#2       R2E,0x00,0x00

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcc\x00\xa1'     # swp#0x1    (R40),R21
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcc\x00\xa1'     # swp#0x1    (R40),R21
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcc\x00\xa1'     # swp#0x1    (R40),R21
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x59\x00\x42'     # ld#0x2     R42,(R40)
    b += b'\x59\x10\xc2'     # ld#0x2     (R50),R42

    b += b'\xc1\x20\x00\x00' # ld#2       R20,0x00,0x00
    b += b'\xc1\x22\xf3\xf4' # ld#2       R22,0xf3,0xf4
    b += b'\xc1\x24\x00\x00' # ld#2       R24,0x00,0x00
    b += b'\xc1\x26\xf7\xf8' # ld#2       R26,0xf7,0xf8
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc1\x30\x11\x12' # ld#2       R30,0x11,0x12
    b += b'\xc1\x32\x13\x14' # ld#2       R32,0x13,0x14
    b += b'\xc1\x34\x15\x16' # ld#2       R34,0x15,0x16
    b += b'\xc1\x36\x17\x18' # ld#2       R36,0x17,0x18
    b += b'\xc1\x38\x19\x1a' # ld#2       R38,0x19,0x1a
    b += b'\xc1\x3a\x1b\x1c' # ld#2       R3A,0x1b,0x1c
    b += b'\xc1\x3c\x1d\x1e' # ld#2       R3C,0x1d,0x1e
    b += b'\xc1\x3e\x1f\x20' # ld#2       R3E,0x1f,0x20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    b += b'\xcf\x00\xa1'     # swp#0x8    (R40),R30
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    b += b'\xc1\x20\x00\x00' # ld#2       R20,0x00,0x00
    b += b'\xc1\x22\xf3\xf4' # ld#2       R22,0xf3,0xf4
    b += b'\xc1\x24\x00\x00' # ld#2       R24,0x00,0x00
    b += b'\xc1\x26\xf7\xf8' # ld#2       R26,0xf7,0xf8
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10
    b += b'\xc1\x30\x11\x12' # ld#2       R30,0x11,0x12
    b += b'\xc1\x32\x13\x14' # ld#2       R32,0x13,0x14
    b += b'\xc1\x34\x15\x16' # ld#2       R34,0x15,0x16
    b += b'\xc1\x36\x17\x18' # ld#2       R36,0x17,0x18
    b += b'\xc1\x38\x19\x1a' # ld#2       R38,0x19,0x1a
    b += b'\xc1\x3a\x1b\x1c' # ld#2       R3A,0x1b,0x1c
    b += b'\xc1\x3c\x1d\x1e' # ld#2       R3C,0x1d,0x1e
    b += b'\xc1\x3e\x1f\x20' # ld#2       R3E,0x1f,0x20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    b += b'\xcf\x00\xa1'     # swp#0x8    (R40),R30
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    # ???
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcc\x80\xa1'     # swp#0x1    (R40),0xa1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcd\x80\xa1'     # swp#0x2    (R40),0xa1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xce\x80\xa1'     # swp#0x4    (R40),0xa1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\xc1\x28\x09\x0a' # ld#2       R28,0x09,0x0a
    b += b'\xc1\x2a\x0b\x0c' # ld#2       R2A,0x0b,0x0c
    b += b'\xc1\x2c\x0d\x0e' # ld#2       R2C,0x0d,0x0e
    b += b'\xc1\x2e\x0f\x10' # ld#2       R2E,0x0f,0x10

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x58\x00\xa0'     # ld#0x1     (R40),R20
    b += b'\xcf\x80\xa1'     # swp#0x8    (R40),0xa1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x42'     # ld#0x8     R42,(R40)
    b += b'\x5b\x10\xc2'     # ld#0x8     (R50),R42

    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'

    # time
    b += b'\xd3\x37'         # ld         DSIZE,0x37
    b += b'\x1b\xe0\x00'     # ld#0x8     R60,0x00
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xf7\xc0'         # timer_ctrl 0xc0
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xb3\x07'         # timer_set  0x07  # 209.34ms
    b += b'\xb9\x00'
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xf7\x80'         # timer_ctrl 0x80
    b += b'\xf7\xc0'         # timer_ctrl 0xc0
    b += b'\xb3\x49'         # timer_set  0x49  # 837.61ms
    b += b'\xb9\x00'
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xfc'             # ?

    b += b'\xf7\x80'         # timer_ctrl 0x80
    b += b'\xf7\xc0'         # timer_ctrl 0xc0
    b += b'\xb3\x49'         # timer_set  0x49  # 837.61ms
    b += b'\xb9\x00'
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60

    b += b'\xfd'             # ?

    # Infinite loop
    b += b'\xff\x88\xf0\x00'
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xb3\x49'         # timer_set  0x49  # 837.61ms
    b += b'\xb9\x00'
    b += b'\xfe'             # timer_wait
    b += b'\xe5\x60'         # ld#0x1     R60,TIME
    b += b'\x5b\x10\xe0'     # ld#0x8     (R50),R60
    b += b'\xff\x88\xf0\x00'

    # ROM check signature
    b += b'\xff' * (0x00fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
