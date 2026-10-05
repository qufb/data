#!/usr/bin/env python3

import sigrokdecode as srd
import sys
import traceback
from functools import reduce


import sigrokdecode as srd

class Pin:
    (
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
    id = "0:data16"
    name = "0:data16"
    longname = "data16"
    desc = "data16"
    license = "mit"
    inputs = ["logic"]
    outputs = []
    tags = ["Embedded"]
    channels = (
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
        ("rom_data", "ROM Data"),
        ("ram_data_r", "RAM Data Read"),
        ("ram_data_w", "RAM Data Write"),
    )
    annotation_rows = (
        ("rom_data", "ROM Data", (0,)),
        ("ram_data_r", "RAM Data Read", (1,)),
        ("ram_data_w", "RAM Data Write", (2,)),
    )

    def reduce_bus(self, bus):
        return reduce(lambda a, b: (a << 1) | b, reversed(bus))

    def reduce_data(self):
        self.wait()
        (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, ce, oe, ram_we, ram_ce) = self.wait()
        #data = self.reduce_bus((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15))
        data = self.reduce_bus((d8, d9, d10, d11, d12, d13, d14, d15, d0, d1, d2, d3, d4, d5, d6, d7))
        self.is_ram_r = ram_we == 1
        return data

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

        while True:
            conds = []
            if self.rom_state == 'start':
                #conds.append({Pin.OE: "f"})
                conds.append({Pin.CE: "f"})
            else:
                #conds.append({Pin.OE: "r"})
                conds.append({Pin.CE: "r"})
            if self.ram_state == 'start':
                #conds.append({Pin.OE: "h", Pin.RAM_CE: "f"})
                #conds.append({Pin.RAM_CE: "f"})
                conds.append({Pin.OE: "h", Pin.RAM_WE: "f"})
            else:
                #conds.append({Pin.OE: "h", Pin.RAM_CE: "r"})
                #conds.append({Pin.RAM_CE: "r"})
                conds.append({Pin.OE: "h", Pin.RAM_WE: "r"})

            self.wait(conds)
            if (self.matched & (0b1 << 0)):
                if self.rom_state == 'start':
                    #self.wait({'skip': 40}) # 20Mhz
                    #self.wait({'skip': 55}) # 20Mhz
                    self.wait({'skip': 70}) # 20Mhz
                    (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, ce, oe, ram_we, ram_ce) = self.wait()
                    ts1_rom_start = self.samplenum
                    rom_data1 = self.reduce_data()
                    self.rom_state = 'end'
                else:
                    ts1_rom_end = self.samplenum
                    self.putx(ts1_rom_start, ts1_rom_end, [0, ["%04x" % (rom_data1)]])
                    self.rom_state = 'start'
            #else:
            if (self.matched & (0b1 << 1)):
                #self.rom_state = 'end'
                if self.ram_state == 'start':
                    # HACK: Ignore false positive spikes
                    self.wait({'skip': 5})
                    (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, ce, oe, ram_we, ram_ce) = self.wait()
                    if ram_we == 0:
                        self.wait({'skip': 10})
                        ts1_ram_start = self.samplenum
                        ram_data1 = self.reduce_data()
                        self.ram_state = 'end'
                else:
                    ts1_ram_end = self.samplenum
                    self.putx(ts1_ram_start, ts1_ram_end, [1 if self.is_ram_r else 2, ["%04x" % (ram_data1)]])
                    self.ram_state = 'start'
