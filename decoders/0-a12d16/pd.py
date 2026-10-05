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
        D0,
        D1,
        D2,
        D3,
        D4,
        D5,
        D6,
        D7,
        D8,
        D9,
        D10,
        D11,
        D12,
        D13,
        D14,
        D15,
        CE,
        OE,
        RAM_WE,
        RAM_CE,
    ) = range(20)


class SamplerateError(Exception):
    pass


class Decoder(srd.Decoder):
    api_version = 3
    id = "0:a12d16"
    name = "0:a12d16"
    longname = "a12d16"
    desc = "a12d16"
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
        {"id": "d0", "name": "D0", "desc": "Data Line 0"},
        {"id": "d1", "name": "D1", "desc": "Data Line 1"},
        {"id": "d2", "name": "D2", "desc": "Data Line 2"},
        {"id": "d3", "name": "D3", "desc": "Data Line 3"},
        {"id": "d4", "name": "D4", "desc": "Data Line 4"},
        {"id": "d5", "name": "D5", "desc": "Data Line 5"},
        {"id": "d6", "name": "D6", "desc": "Data Line 6"},
        {"id": "d7", "name": "D7", "desc": "Data Line 7"},
        {"id": "d8", "name": "D8", "desc": "Data Line 8"},
        {"id": "d9", "name": "D9", "desc": "Data Line 9"},
        {"id": "d10", "name": "D10", "desc": "Data Line 10"},
        {"id": "d11", "name": "D11", "desc": "Data Line 11"},
        {"id": "d12", "name": "D12", "desc": "Data Line 12"},
        {"id": "d13", "name": "D13", "desc": "Data Line 13"},
        {"id": "d14", "name": "D14", "desc": "Data Line 14"},
        {"id": "d15", "name": "D15", "desc": "Data Line 15"},
        {"id": "ce", "name": "CE", "desc": "Chip Enable"},
        {"id": "oe", "name": "OE", "desc": "Output Enable"},
        {"id": "ram_we", "name": "RAM_WE", "desc": "RAM Write Enable"},
        {"id": "ram_ce", "name": "RAM_CE", "desc": "RAM Chip Enable"},
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
        self.wait()
        (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, ce, oe, ram_we, ram_ce) = self.wait()
        addr = self.reduce_bus((a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11))
        data = self.reduce_bus((d8, d9, d10, d11, d12, d13, d14, d15, d0, d1, d2, d3, d4, d5, d6, d7))
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
                # conds.append({Pin.OE: "f"})
                conds.append({Pin.CE: "f"})
            else:
                # conds.append({Pin.OE: "r"})
                conds.append({Pin.CE: "r"})
            if self.ram_state == 'start':
                # conds.append({Pin.OE: "h", Pin.RAM_CE: "f"})
                # conds.append({Pin.RAM_CE: "f"})
                conds.append({Pin.RAM_WE: "f"})
            else:
                # conds.append({Pin.OE: "h", Pin.RAM_CE: "r"})
                # conds.append({Pin.RAM_CE: "r"})
                conds.append({Pin.RAM_WE: "r"})

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
            #else:
            if (self.matched & (0b1 << 1)):
                #self.rom_state = 'end'
                if self.ram_state == 'start':
                    # HACK (due to no RAM_OE)
                    # 25/1.67 ~= 15, need half+delta of that
                    # self.wait({'skip': 10})
                    self.wait({'skip': 15})
                    ts1_ram_start = self.samplenum
                    ram_addr1, ram_data1 = self.reduce_addr_data()
                    self.ram_state = 'end'
                else:
                    ts1_ram_end = self.samplenum
                    self.putx(ts1_ram_start, ts1_ram_end, [2, ["%06x" % (ram_addr1 * 2)]])
                    self.putx(ts1_ram_start, ts1_ram_end, [3 if self.is_ram_r else 4, ["%04x" % (ram_data1)]])
                    self.ram_state = 'start'
            #if (self.matched & (0b1 << 1)):
            #    #self.rom_state = 'end'
            #    if self.ram_state == 'start':
            #        # HACK: Ignore false positive spikes
            #        self.wait({'skip': 5})
            #        (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, ce, oe, ram_we, ram_ce) = self.wait()
            #        if ram_we == 0:
            #            self.wait({'skip': 10})
            #            ts1_ram_start = self.samplenum
            #            ram_data1 = self.reduce_data()
            #            self.ram_state = 'end'
            #    else:
            #        ts1_ram_end = self.samplenum
            #        self.putx(ts1_ram_start, ts1_ram_end, [1 if self.is_ram_r else 2, ["%04x" % (ram_data1)]])
            #        self.ram_state = 'start'
