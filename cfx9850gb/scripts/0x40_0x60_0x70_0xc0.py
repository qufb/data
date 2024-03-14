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

    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40

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

    # 0x40..0x44
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x40\x80'         # shr#0x1    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x40\x80'         # shr#0x1    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x41\x00'         # shl#0x2    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x41\x00'         # shl#0x2    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x42\x80'         # shr#0x4    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x42\x80'         # shr#0x4    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x43\x00'         # shl#0x8    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x43\x00'         # shl#0x8    (R40),8
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    # 0x48..0x4b
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x48\x80'         # shr#0x1    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x48\x80'         # shr#0x1    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x49\x00'         # shl#0x2    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x49\x00'         # shl#0x2    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x4a\x80'         # shr#0x4    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x4a\x80'         # shr#0x4    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x4b\x00'         # shl#0x8    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x4b\x00'         # shl#0x8    (R40),4
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    


    # 0x60..0x64
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x60\x80'         # shr#0x1    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x60\x80'         # shr#0x1    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x61\x00'         # shl#0x2    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x61\x00'         # shl#0x2    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x62\x80'         # shr#0x4    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x62\x80'         # shr#0x4    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x63\x00'         # shl#0x8    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x63\x00'         # shl#0x8    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    # 0x68..0x6b
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x68\x80'         # shr#0x1    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x68\x80'         # shr#0x1    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x69\x00'         # shl#0x2    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x69\x00'         # shl#0x2    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x6a\x80'         # shr#0x4    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x6a\x80'         # shr#0x4    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x6b\x00'         # shl#0x8    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x6b\x00'         # shl#0x8    (R40),1
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    # 0x70..0x74
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x70\x00\xa0'     # sbb#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x70\x00\xa0'     # sbb#0x1    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x71\x00\xa0'     # sbb#0x2    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x71\x00\xa0'     # sbb#0x2    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x72\x00\xa0'     # sbb#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x72\x00\xa0'     # sbb#0x4    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20
    
    b += b'\xd9\x00'         # ld         F,0x0
    b += b'\x73\x00\xa0'     # sbb#0x8    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40
    
    b += b'\xc1\x1e\xfe\xff' # ld#2       R1E,0xfe,0xff
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    b += b'\x73\x00\xa0'     # sbb#0x8    (R40),R20
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'



    # 0xc0
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc0\x20' + bytes([i]) + b'\xff' # ld#1  R20,0x??
        b += b'\xc0\xa0' + bytes([i]) + b'\xff' # ld#1  R20,0x??
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc0' + bytes([i]) + b'\x20\xff' # ld#1  R??,0x20
        b += b'\xc0' + bytes([i]) + b'\xa0\xff' # ld#1  R??,0xa0
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'



    # 0xc2
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc2\x20' + bytes([i]) + b'\xff\xff\xff\xff' # ld#8  R20,0x??
        b += b'\xc2\xa0' + bytes([i]) + b'\xff\xff\xff\xff' # ld#8  R20,0x??
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc2' + bytes([i]) + b'\x20\xff\xff\xff\xff' # ld#8  R??,0x20
        b += b'\xc2' + bytes([i]) + b'\xa0\xff\xff\xff\xff' # ld#8  R??,0xa0
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x00\x20'     # ld#0x8     R20,(R40)
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40



    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'
    b += b'\xff\xff\xff\xff'

    b += b'\xd3\x37'
    b += b'\xd5\x08'
    b += b'\xd7\xff\x2f'
    b += b'\xd9\x3f'
    b += b'\xdb\x7b\xff\xff'
    b += b'\xdd\x40'
    b += b'\xde\x7f\xff'

    b += b'\xe0\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe1\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe2\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe3\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe4\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe5\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe6\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe7\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe8\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe9\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xea\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xeb\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xec\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xed\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xee\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xef\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20

    # 0xc3
    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc3\x20' + bytes([i]) + b'\xff' # ld#8  R20,0x??
        b += b'\xc3\xa0' + bytes([i]) + b'\xff' # ld#8  R20,0x??
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40

    b += b'\xc1\x20\x01\x02' # ld#2       R20,0x01,0x02
    b += b'\xc1\x22\x03\x04' # ld#2       R22,0x03,0x04
    b += b'\xc1\x24\x05\x06' # ld#2       R24,0x05,0x06
    b += b'\xc1\x26\x07\x08' # ld#2       R26,0x07,0x08
    b += b'\x5b\x00\xa0'     # ld#0x8     (R40),R20

    b += b'\xd9\xff'         # ld         F,0xff
    for i in range(0x100):
        b += b'\xc3' + bytes([i]) + b'\x20\xff' # ld#8  R??,0x20
        b += b'\xc3' + bytes([i]) + b'\xa0\xff' # ld#8  R??,0xa0
    b += b'\xe4\x7f'         # ld         R7F,F
    b += b'\x58\x10\xff'     # ld#0x1     (R50),R7F
    b += b'\x5b\x10\xa0'     # ld#0x8     (R50),R20
    b += b'\x5b\x10\xc0'     # ld#0x8     (R50),R40
    b += b'\xc1\x40\x40\x40' # ld#2       R40,0x40,0x40

    b += b'\xe0\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe1\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe2\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe3\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe4\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe5\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe6\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe7\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe8\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xe9\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xea\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xeb\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xec\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xed\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xee\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20
    b += b'\xef\x20'
    b += b'\x59\x00\xa0'     # ld#0x2     (R40),R20



    # Infinite loop
    b += b'\xff\x88\xf0\x00'
    b += b'\xff' * (0x00f000 - len(b))
    b += b'\xff\x88\xf0\x00'

    # ROM check signature
    b += b'\xff' * (0x00fff0 - len(b))
    b += b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Blank
    b += b'\xff' * (0x100000 - len(b))

    f.write(b)
