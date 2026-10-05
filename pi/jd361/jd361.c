#include "hardware/gpio.h"
#include "hardware/sync.h"
#include "pico/binary_info.h"
#include "pico/stdlib.h"
#include <stdio.h>

#define NUM_ADDR 16
#define NUM_DATA 8

const int D0_PIN = 0;
const int D1_PIN = 1;
const int D2_PIN = 2;
const int D3_PIN = 3;
const int D4_PIN = 4;
const int D5_PIN = 5;
const int D6_PIN = 6;
const int D7_PIN = 7;

const int A0_PIN = 8;
const int A1_PIN = 9;
const int A2_PIN = 10;
const int A3_PIN = 11;
const int A4_PIN = 12;
const int A5_PIN = 13;
const int A6_PIN = 14;
const int A7_PIN = 15;
const int A8_PIN = 16;
const int A9_PIN = 17;
const int A10_PIN = 18;
const int A11_PIN = 19;
const int A12_PIN = 20;
const int A13_PIN = 21;
const int A14_PIN = 22;
const int A15_PIN = 26;
// A16..A18 are manually pulled on each dump;

const int LSB_PIN = 27;  // a.k.a. Q15/A-1
const int CE_OE_PIN = 28;
// ~BYTE is pulled-low;
// ~WE is pulled-high;
// ~WP is pulled-high;

const int address_pins[NUM_ADDR] = {
    A0_PIN,
    A1_PIN,
    A2_PIN,
    A3_PIN,
    A4_PIN,
    A5_PIN,
    A6_PIN,
    A7_PIN,
    A8_PIN,
    A9_PIN,
    A10_PIN,
    A11_PIN,
    A12_PIN,
    A13_PIN,
    A14_PIN,
    A15_PIN
};

const int data_pins[NUM_DATA] = {
    D0_PIN,
    D1_PIN,
    D2_PIN,
    D3_PIN,
    D4_PIN,
    D5_PIN,
    D6_PIN,
    D7_PIN,
};

#define BUFFER_SIZE 128

uint8_t buffer[BUFFER_SIZE] = { 0 };

void sleep_ns(uint32_t ns) {
    // - Pico:   125MHz => 8ns
    // - Pico 2: 150MHz => ~6.667ns

    int extra = 2;
    double factor = 6.6;
    uint32_t times = (ns / factor) + extra;
    for (int i = 0; i < times; i++) {
        __nop();
    }
    
   //sleep_ms(1);
}

void print8(uint8_t value) { printf("%02x", value); }

void print32(uint32_t value) {
    print8((value >> 24) & 0xFF);
    print8((value >> 16) & 0xFF);
    print8((value >> 8) & 0xFF);
    print8((value >> 0) & 0xFF);
}

void set_address(uint32_t addr) {
    if ((addr & 1) == 1) {
        gpio_put(LSB_PIN, 1);
    } else {
        gpio_put(LSB_PIN, 0);
    }
    addr = addr >> 1;

    sleep_ns(120);  // ~BYTE to output delay time (unspecified, based on MX29L1611-12)

    for (int i = 0; i < NUM_ADDR; i++) {
        if (addr & (1 << i)) {
            gpio_put(address_pins[i], 1);
        } else {
            gpio_put(address_pins[i], 0);
        }
    }
}

// Based on TC534000P
uint8_t read_data(uint32_t addr) {
    set_address(addr);

    sleep_ns(250);  // Address access time

    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 0);

    sleep_ns(350);  // Chip enable + output enable access time

    uint8_t result = 0;
    for (int i = 0; i < NUM_DATA; i++) {
        if (gpio_get(data_pins[i])) {
            result |= (1 << i);
        }
    }

    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 1);

    sleep_ns(80);  // Output disable time

    return result;
}

void init() {
    for (int i = 0; i < NUM_ADDR; i++) {
        gpio_init(address_pins[i]);
        gpio_set_dir(address_pins[i], GPIO_OUT);
    }
    for (int i = 0; i < NUM_DATA; i++) {
        gpio_init(data_pins[i]);
        gpio_set_dir(data_pins[i], GPIO_IN);
    }

    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 1);

    gpio_init(LSB_PIN);
    gpio_set_dir(LSB_PIN, GPIO_OUT);
    gpio_put(LSB_PIN, 1);
}

void dump(uint32_t bankSize, uint32_t cartSize) {
    printf("START\n");

    for (int currBank = 0; currBank < (cartSize / bankSize); currBank++) {
        for (uint32_t currBuffer = 0; currBuffer < bankSize; currBuffer += BUFFER_SIZE) {
            for (uint16_t currByte = 0; currByte < BUFFER_SIZE; currByte++) {
                buffer[currByte] = read_data((bankSize * currBank) + (unsigned long)(currBuffer + currByte));
            }

            for (uint16_t xi = 0; xi < BUFFER_SIZE; xi++) {
                if (xi % 16 == 0) {
                    uint32_t addr = (uint32_t)(xi + currBuffer) + (bankSize * currBank);
                    print32(addr);
                    printf(" ");
                }
                print8(buffer[xi]);
                if (xi > 0 && ((xi + 1) % 16) == 0) {
                    printf("\n");
                } else {
                    printf(" ");
                }
            }
        }
    }

    printf("END\n");
}

void dump_all() {
    uint32_t bankSize = 16 * 1024UL;
    uint32_t cartSize = 128 * 1024UL;
    dump(bankSize, cartSize);
}

void dump_128() {
    uint32_t bankSize = BUFFER_SIZE;
    uint32_t cartSize = BUFFER_SIZE;
    dump(bankSize, cartSize);
}

void dump_256() {
    uint32_t bankSize = 2 * BUFFER_SIZE;
    uint32_t cartSize = 2 * BUFFER_SIZE;
    dump(bankSize, cartSize);
}

int main() {
    stdio_init_all();
    init();

    while (true) {
        sleep_ms(200);

        printf("Press any key to start dump.\n");
        
        int c;
        if ((c = getchar()) != PICO_ERROR_TIMEOUT) {
            dump_128();
            //dump_256();
            //dump_all();
        }
    }
}
