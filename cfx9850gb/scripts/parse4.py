#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'rb') as f:
    dump = f.read()

for i in range(0, len(dump), 4):
    d = {}
    for j in range(4):
        b = dump[i+j]
        if b not in d:
            d[b] = 0
        d[b] += 1
    if (len(d) > 1):
        o = ''
        for k, v in d.items():
            o += f"{k:02x}:{v} "
        print(f"Bad read @ {i:08x}: {o}", file=sys.stderr)
    v = max(d, key=d.get)
    sys.stdout.buffer.write(bytes([v]))
