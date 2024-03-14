#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'rb') as f:
    dump = f.read()

for i in range(0, len(dump), 8):
    d = {}
    for j in range(8):
        b = dump[i+j]
        if b not in d:
            d[b] = 0
        d[b] += 1
    if (len(d) > 1):
        print(f"Bad read @ {hex(i)}: {d}", file=sys.stderr)
    v = max(d, key=d.get)
    sys.stdout.buffer.write(bytes([v]))
