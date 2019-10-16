#include <stdio.h>
#include <string.h>
#include "Cfile.h"



int fun1(int x, int *y, const int *z){
    printf("Value of int X:         %d\n", x);
    printf("Value of int *Y:        %d\n", *y);
    printf("Value of const int *Z:  %d\n", *z);
    return 1;
}

int fun11(double x, double *y){
    printf("Value of double  X:         %f\n", x);
    printf("Value of double *Y:         %f\n", *y);
    return 1;
}

int fun12(double x[], int arrlen){

    int  i = 0;
    printf("Running the double array ..\n");
    for(i = 0; i<arrlen; i++){
        printf("Value of double X at %d is: %f\n", i, x[i]);
    }
    return 1;
}


int fun2(const int *sockfd, const int *flaWri, int *flaRea,
            const int *nDblWri, int *nDblRea,
            double *simTimWri, double dblValWri[],
            double *simTimRea, double dblValRea[])
{

    printf("Value of const int    *sockfd:  %d\n", *sockfd);
    printf("Value of const int    *flaWri:  %d\n", *flaWri);
    printf("Value of       int    *flaRea:  %d\n", *flaRea);
    printf("Value of const int    *nDblWri:  %d\n", *nDblWri);
    printf("Value of       int    *nDblRea:  %d\n", *nDblRea);
    printf("Value of       double *simTimWri:%f\n", *simTimWri);
    printf("Value of       double *simTimRea:%f\n", *simTimRea);
    
    int i = 0;
    printf("Running the dblValWri array ..\n");
    for(i = 0; i<*nDblWri; i++){
        printf("Value of double dblValWri at %d is: %f\n", i, dblValWri[i]);
    }
    printf("Running the dblValWri array ..\n");
    for(i = 0; i<*nDblRea; i++){
        printf("Value of double dblValRea at %d is: %f\n", i, dblValRea[i]);
    }

    return 1;
}


int fun13(const char *const msg)
{
    printf("The value of msg: %s \n", msg);
    return 2;
}

int randomFunction(){
    printf("This is an empty function to test...\n");
    return 1;
}


int main(){
    fprintf(stderr, "Calling established...'\n");
    return 0;
}
