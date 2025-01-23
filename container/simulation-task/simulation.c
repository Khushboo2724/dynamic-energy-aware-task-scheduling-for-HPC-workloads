#include <stdio.h>
#include <omp.h>

#define SIZE 1000000

void run_simulation() {
    double result = 0.0;
    #pragma omp parallel for reduction(+:result)
    for (int i = 0; i < SIZE; i++) {
        result += 1.0 / (i + 1);
    }
    printf("Result of simulation: %f\n", result);
}

int main() {
    run_simulation();
    return 0;
}
