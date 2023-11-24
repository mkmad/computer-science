#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define MAX_FILENAME_LEN 100
#define INPUT_SIZE 10000
#define MUTATION_RATE 0.13
#define EXTEND_INTERVAL 500
#define EXTEND_AMOUNT 10

void mutate_input(unsigned char *input, int size) {
    for (int i = 0; i < size; i++) {
        if ((double)rand() / RAND_MAX < MUTATION_RATE) {
            input[i] = (unsigned char)(rand() % 256);
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s prng_seed num_of_iterations\n", argv[0]);
        return 1;
    }

    uint32_t prng_seed = (uint32_t)atoi(argv[1]);
    uint32_t num_iterations = (uint32_t)atoi(argv[2]);

    srand(prng_seed);
    srand48(prng_seed);

    FILE *seed_file = fopen("_seed_", "rb");
    if (seed_file == NULL) {
        fprintf(stderr, "Error opening seed file.\n");
        return 1;
    }

    unsigned char input[INPUT_SIZE];
    size_t input_len = fread(input, 1, INPUT_SIZE, seed_file);
    fclose(seed_file);

    for (uint32_t i = 1; i <= num_iterations; i++) {
        mutate_input(input, input_len);

        if (i % EXTEND_INTERVAL == 0 && input_len + EXTEND_AMOUNT < INPUT_SIZE) {
            for (int j = 0; j < EXTEND_AMOUNT; j++) {
                input[input_len++] = (unsigned char)(rand() % 256);
            }
        }
    }

    fwrite(input, 1, input_len, stdout);

    return 0;
}
