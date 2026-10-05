# Logic analyzer decoders + data analysis

Traces were captured with a DSLogic U3Pro32. Note that A3 channel is delayed by a few ns compared to other channels...

## cfx9850gb

* [dsl](./cfx9850gb/dsl): Various instruction traces. CLK signal is also sampled for inferring instruction timings.
* [scripts](./cfx9850gb/scripts): Internal CPU ROM dumping and instruction analysis.

## decoders

* [hcd62121](./decoders/0-hcd62121): Used for cfx9850gb traces;
* [rom8](./decoders/0-rom8): Similar to 0-hcd62121 but assuming `/BYTE` is high (data in 8-bit mode);
* [a22](./decoders/0-a22): 22 address + 8 data lines;
* [a12d16](./decoders/0-a12d16): 12 address + 16 data lines;
* [data16](./decoders/0-data16): 16 data lines;

Note that several of these have hardcoded cycle waits after `/CE` and `/OE` were asserted. These are intended to workaround older ICs that are slower to stabilize read data. Apparently off-the-shelf programmers don't have configurable timings for anything besides flash...

## pi

* [rom32m](./pi/rom32m/): Assert address lines with hardcoded timings;
* [rom32rep](./pi/rom32rep/): Only assert specific addresses N times;

Setup:

1. Install VSCode extension for Raspberry Pi Pico;
1. Copy decoders to `DSView-1.3.1/libsigrokdecode4DSL/decoders/`;
1. Run `make && sudo make install && DSView`;

Workflow without trigger signals ([example](https://qufb.gitlab.io/writeups/casiolcd)):

1. Power-on IC;
1. Start DSLogic capture;
1. Start Pi dumping (e.g. user input via `picocom -b 115200 /dev/ttyACM0`);
1. Stop DSLogic capture;
1. Export CSV with ROM address + data columns;
1. Parse binary (e.g. `tail -n+2 decoder--260101-123456.csv | cut -d',' -f3 | paste -sd '' | xxd -r -p > foo.bin`);
