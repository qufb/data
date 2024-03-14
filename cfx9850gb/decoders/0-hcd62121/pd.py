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
        CLK,
        CE,
        OE,
        RAM_WE,
        RAM_CE,
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
    id = "0:hcd62121"
    name = "0:HCD62121"
    longname = "HCD62121"
    desc = "HCD62121"
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
        {"id": "clk", "name": "CLK", "desc": "CPU Clock"},
        {"id": "ce", "name": "CE", "desc": "Chip Enable"},
        {"id": "oe", "name": "OE", "desc": "Output Enable"},
        {"id": "ram_we", "name": "RAM_WE", "desc": "RAM Write Enable"},
        {"id": "ram_ce", "name": "RAM_CE", "desc": "RAM Chip Enable"},
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
        ("ram_addr", "RAM Address"),
        ("ram_data_r", "RAM Data Read"),
        ("ram_data_w", "RAM Data Write"),
    )
    annotation_rows = (
        ("rom_addr", "ROM Address", (0,)),
        ("rom_data", "ROM Data", (1,)),
        ("ram_addr", "RAM Address", (2,)),
        ("ram_data_r", "RAM Data Read", (3,)),
        ("ram_data_w", "RAM Data Write", (4,)),
    )

    def reduce_bus(self, bus):
        return reduce(lambda a, b: (a << 1) | b, reversed(bus))

    def reduce_addr_data(self):
        (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, clk, ce, oe, ram_we, ram_ce, d0, d1, d2, d3, d4, d5, d6, d7,) = self.wait({Pin.CLK: "r"})
        addr = self.reduce_bus((a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18,))
        data = self.reduce_bus((d0, d1, d2, d3, d4, d5, d6, d7))
        self.is_ram_r = ram_we == 1
        return addr, data

    def putx(self, sample_start, sample_end, data):
        self.put(sample_start, sample_end, self.out_ann, data)

    def __init__(self):
        self.reset()

    def reset(self):
        self.is_ram_r = True
        self.ram_state = 'start'
        self.rom_state = 'start'

    def start(self):
        self.out_ann = self.register(srd.OUTPUT_ANN)

    def metadata(self, key, value):
        if key == srd.SRD_CONF_SAMPLERATE:
            self.samplerate = value

    def decode(self):
        if not self.samplerate:
            raise SamplerateError("Cannot decode without samplerate.")

        i = 0
        while True:
            conds = []
            if self.rom_state == 'start':
                conds.append({Pin.OE: "f"})
            else:
                conds.append({Pin.OE: "r"})
            if self.ram_state == 'start':
                conds.append({Pin.OE: "h", Pin.RAM_CE: "f"})
            else:
                conds.append({Pin.OE: "h", Pin.RAM_CE: "r"})

            self.wait(conds)
            if (self.matched & (0b1 << 0)):
                if self.rom_state == 'start':
                    if i == 0:
                        ts1_rom_start = self.samplenum
                        rom_addr1, rom_data1 = self.reduce_addr_data() # FIXME: Should be on OE: "r"?
                        i += 1
                    else:
                        ts2_rom_start = self.samplenum
                        rom_addr2, rom_data2 = self.reduce_addr_data()
                        i += 1
                    self.rom_state = 'end'
                else:
                    if i == 1:
                        ts1_rom_end = self.samplenum
                    elif i == 2:
                        ts2_rom_end = self.samplenum
                        if rom_addr1 == rom_addr2:
                            # ROM pin 33 (nBYTE) is always pulled low, therefore
                            # always decode data in 16-bit mode
                            self.putx(ts1_rom_start, ts2_rom_end, [0, ["%06x" % (rom_addr1 * 2)]])
                            self.putx(ts1_rom_start, ts2_rom_end, [1, ["%04x" % ((rom_data1 << 8) | rom_data2)]])
                            i -= 2
                        else:
                            self.putx(ts1_rom_start, ts1_rom_end, [0, ["%06x" % (rom_addr1 * 2)]])
                            self.putx(ts1_rom_start, ts1_rom_end, [1, ["%02x" % (rom_data1)]])
                            i -= 1
                        ts1_rom_start = ts2_rom_start
                        ts1_rom_end = ts2_rom_end
                        rom_addr1 = rom_addr2
                        rom_data1 = rom_data2
                    self.rom_state = 'start'
            else:
                if self.ram_state == 'start':
                    ts1_ram_start = self.samplenum
                    ram_addr1, ram_data1 = self.reduce_addr_data()
                    self.ram_state = 'end'
                else:
                    ts1_ram_end = self.samplenum
                    self.putx(ts1_ram_start, ts1_ram_end, [2, ["%06x" % (ram_addr1 * 2)]])
                    self.putx(ts1_ram_start, ts1_ram_end, [3 if self.is_ram_r else 4, ["%02x" % (ram_data1)]])
                    self.ram_state = 'start'
