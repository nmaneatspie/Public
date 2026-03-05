//cc -fPIC -shared -o csort.so csort.c
// sort int array
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int comp_ascend(const void *a, const void *b) {
    
    const int *A = a, *B = b;
    return (*A > *B) - (*B > *A);
    //return (*A - *B);
}

int comp_descend(const void *a, const void *b) {
    
    const int *A = a, *B = b;
    return (*A < *B) - (*B < *A);
    //return (*B - *A);
}


extern void sort(int* inArr, const size_t size, const char order){
// inArr is int array to sort, size is the length of the array
//order is the 0 for ascending or 1/otherwise for ascending

    if(!order){
        qsort(inArr,size, sizeof(inArr[0]), comp_ascend);
    }
    else {
        qsort(inArr, size, sizeof(inArr[0]), comp_descend);
    }
    
}


int main()
{
    return 0;
}