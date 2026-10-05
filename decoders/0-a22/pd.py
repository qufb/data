#!/usr/bin/env python3

import sigrokdecode as srd
import sys
import traceback
from functools import reduce


import sigrokdecode as srd


class Pin:
    (
        A0,
        A1,
        A2,
        A3,
        A4,
        A5,
        A6,
        A7,
        A8,
        A9,
        A10,
        A11,
        A12,
        A13,
        A14,
        A15,
        A16,
        A17,
        A18,
        A19,
        A20,
        A21,
        CE,
        OE,
        D0,
        D1,
        D2,
        D3,
        D4,
        D5,
        D6,
        D7,
    ) = range(32)


class SamplerateError(Exception):
    pass


class Decoder(srd.Decoder):
    api_version = 3
    id = "0:a22"
    name = "0:a22"
    longname = "a22"
    desc = "a22"
    license = "mit"
    inputs = ["logic"]
    outputs = []
    tags = ["Embedded"]
    channels = (
        {"id": "a0", "name": "A0", "desc": "Address Line 0"},
        {"id": "a1", "name": "A1", "desc": "Address Line 1"},
        {"id": "a2", "name": "A2", "desc": "Address Line 2"},
        {"id": "a3", "name": "A3", "desc": "Address Line 3"},
        {"id": "a4", "name": "A4", "desc": "Address Line 4"},
        {"id": "a5", "name": "A5", "desc": "Address Line 5"},
        {"id": "a6", "name": "A6", "desc": "Address Line 6"},
        {"id": "a7", "name": "A7", "desc": "Address Line 7"},
        {"id": "a8", "name": "A8", "desc": "Address Line 8"},
        {"id": "a9", "name": "A9", "desc": "Address Line 9"},
        {"id": "a10", "name": "A10", "desc": "Address Line 10"},
        {"id": "a11", "name": "A11", "desc": "Address Line 11"},
        {"id": "a12", "name": "A12", "desc": "Address Line 12"},
        {"id": "a13", "name": "A13", "desc": "Address Line 13"},
        {"id": "a14", "name": "A14", "desc": "Address Line 14"},
        {"id": "a15", "name": "A15", "desc": "Address Line 15"},
        {"id": "a16", "name": "A16", "desc": "Address Line 16"},
        {"id": "a17", "name": "A17", "desc": "Address Line 17"},
        {"id": "a18", "name": "A18", "desc": "Address Line 18"},
        {"id": "a19", "name": "A19", "desc": "Address Line 19"},
        {"id": "a20", "name": "A20", "desc": "Address Line 20"},
        {"id": "a21", "name": "A21", "desc": "Address Line 21"},
        {"id": "ce", "name": "CE", "desc": "Chip Enable"},
        {"id": "oe", "name": "OE", "desc": "Output Enable"},
        {"id": "d0", "name": "D0", "desc": "Data Line 0"},
        {"id": "d1", "name": "D1", "desc": "Data Line 1"},
        {"id": "d2", "name": "D2", "desc": "Data Line 2"},
        {"id": "d3", "name": "D3", "desc": "Data Line 3"},
        {"id": "d4", "name": "D4", "desc": "Data Line 4"},
        {"id": "d5", "name": "D5", "desc": "Data Line 5"},
        {"id": "d6", "name": "D6", "desc": "Data Line 6"},
        {"id": "d7", "name": "D7", "desc": "Data Line 7"},
    )
    optional_channels = ()
    options = ()
    annotations = (
        ("rom_addr", "ROM Address"),
        ("rom_data", "ROM Data"),
    )
    annotation_rows = (
        ("rom_addr", "ROM Address", (0,)),
        ("rom_data", "ROM Data", (1,)),
    )

    def reduce_bus(self, bus):
        return reduce(lambda a, b: (a << 1) | b, reversed(bus))

    def reduce_addr_data(self):
        self.wait()
        (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, ce, oe, d0, d1, d2, d3, d4, d5, d6, d7,) = self.wait()
        addr = self.reduce_bus((a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21))
        data = self.reduce_bus((d0, d1, d2, d3, d4, d5, d6, d7))
        return addr, data

    def putx(self, sample_start, sample_end, data):
        self.put(sample_start, sample_end, self.out_ann, data)

    def __init__(self):
        self.reset()

    def reset(self):
        self.rom_state = 'start'

    def start(self):
        self.out_ann = self.register(srd.OUTPUT_ANN)

    def metadata(self, key, value):
        if key == srd.SRD_CONF_SAMPLERATE:
            self.samplerate = value

    def decode(self):
        if not self.samplerate:
            raise SamplerateError("Cannot decode without samplerate.")

        while True:
            conds = []
            if self.rom_state == 'start':
                #conds.append({Pin.CE: "f"})
                conds.append({Pin.OE: "f"})
            else:
                #conds.append({Pin.CE: "r"})
                conds.append({Pin.OE: "r"})

            self.wait(conds)
            if (self.matched & (0b1 << 0)):
                if self.rom_state == 'start':
                    ts1_rom_start = self.samplenum
                    rom_addr1, rom_data1 = self.reduce_addr_data()
                    self.rom_state = 'end'
                else:
                    ts1_rom_end = self.samplenum
                    self.putx(ts1_rom_start, ts1_rom_end, [0, ["%06x" % (rom_addr1)]])
                    self.putx(ts1_rom_start, ts1_rom_end, [1, ["%02x" % (rom_data1)]])
                    self.rom_state = 'start'
