#include "hardware/gpio.h"
#include "hardware/sync.h"
#include "pico/binary_info.h"
#include "pico/stdlib.h"
#include <stdio.h>

//#define NUM_ADDR 18
#define NUM_ADDR 23
#define NUM_PINS 25

const int A0_PIN = 0;
const int A1_PIN = 1;
const int A2_PIN = 2;
const int A3_PIN = 3;
const int A4_PIN = 4;
const int A5_PIN = 5;
const int A6_PIN = 6;
const int A7_PIN = 7;
const int A8_PIN = 8;
const int A9_PIN = 9;
const int A10_PIN = 10;
const int A11_PIN = 11;
const int A12_PIN = 12;
const int A13_PIN = 13;
const int A14_PIN = 14;
const int A15_PIN = 15;
const int A16_PIN = 16;
const int A17_PIN = 17;
const int A18_PIN = 18;
const int A19_PIN = 19;
const int A20_PIN = 20;
const int A21_PIN = 21;
const int A22_PIN = 22;
const int A23_PIN = 26;
const int A24_PIN = 27;

const int CE_OE_PIN = 28;

const int address_pins[NUM_PINS] = {
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
    A15_PIN,
    A16_PIN,
    A17_PIN,
    A18_PIN,
    A19_PIN,
    A20_PIN,
    A21_PIN,
    A22_PIN,
    A23_PIN,
    A24_PIN,
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
void read_data(uint32_t addr) {
    set_address(addr);

    //sleep_ns(250);  // Address access time
    // mb838200l access time = max 400ns @ 3v
    sleep_ns(450);  // Address access time
 
    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 0);

    //sleep_ns(350);  // Chip enable + output enable access time
    // LA has lag on D3...
    //sleep_ns(550);  // Chip enable + output enable access time
    sleep_ns(950);  // Chip enable + output enable access time

    // Skip read: done by logic analyzer

    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 1);

    sleep_ns(80);  // Output disable time
}

void init() {
    for (int i = 0; i < NUM_ADDR; i++) {
        gpio_init(address_pins[i]);
        gpio_set_dir(address_pins[i], GPIO_OUT);
    }

    gpio_init(CE_OE_PIN);
    gpio_set_dir(CE_OE_PIN, GPIO_OUT);
    gpio_put(CE_OE_PIN, 1);
}

void dump16n(uint32_t at) {
    uint32_t base = at & 0xfffffff8UL;
    printf("START @ %08x\n", base);

    for (uint8_t n = 0; n < 20; n++) {
        for (uint32_t i = 0; i < 8; i++) {
            uint32_t addr = base + i;
            read_data(addr);
        }
    }

    printf("END\n");
}

void dump(uint32_t bankSize, uint32_t cartSize) {
    printf("START\n");

    for (int currBank = 0; currBank < (cartSize / bankSize); currBank++) {

        uint32_t addr = bankSize * currBank;
        print32(addr);
        printf("\n");

        for (uint32_t currBuffer = 0; currBuffer < bankSize; currBuffer += BUFFER_SIZE) {
            for (uint16_t currByte = 0; currByte < BUFFER_SIZE; currByte++) {
                read_data((bankSize * currBank) + (unsigned long)(currBuffer + currByte));
            }

            /*
            for (uint16_t xi = 0; xi < BUFFER_SIZE; xi++) {
                if (xi % 16 == 0) {
                    uint32_t addr = (uint32_t)(xi + currBuffer) + (bankSize * currBank);
                    print32(addr);
                    printf(" ");
                }
                if (xi > 0 && ((xi + 1) % 16) == 0) {
                    printf("\n");
                }
            }
            */
        }
    }

    printf("END\n");
}


void dump_ofs(uint32_t bankSize, uint32_t cartSize, uint32_t ofs) {
    printf("START\n");

    for (int currBank = 0; currBank < (cartSize / bankSize); currBank++) {

        uint32_t addr = ofs + (bankSize * currBank);
        print32(addr);
        printf("\n");

        for (uint32_t currBuffer = 0; currBuffer < bankSize; currBuffer += BUFFER_SIZE) {
            for (uint16_t currByte = 0; currByte < BUFFER_SIZE; currByte++) {
                read_data(addr + (unsigned long)(currBuffer + currByte));
            }
        }
    }

    printf("END\n");
}

void dump_all() {
    uint32_t bankSize = 16 * 1024UL;
    //uint32_t cartSize = 128 * 1024UL;
    uint32_t cartSize = (1UL << NUM_ADDR);
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
            //dump_128();
            //dump_256();

            dump_all();

            /*
            for (size_t i = 0; i < 1; i++) {
                dump_ofs(16 * 1024UL, 0x8000UL, 0x200000UL);
            }
            */
        }
    }
}
