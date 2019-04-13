#include <stdio.h>
#include <gsl/gsl_ieee_utils.h>

int main() {
    float * floatPointer;
    float f = 1.5;
    float divider = 2.0;
    floatPointer = &f;

    for (int i=0; i<200; i++){
        gsl_ieee_printf_float(floatPointer);
        f = f/divider;
    }

    return 0;
}
