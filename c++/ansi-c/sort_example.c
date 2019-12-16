#include <stdio.h>
#include <stdlib.h>

double values[] = { 88.0, 56.0, 100.1, 2.0, 25.0 };

int compare_doubles(const void *a, const void *b) {
    double *x = (double *) a;
    double *y = (double *) b;
    if      (*x < *y)  { return -1; }
    else if (*x > *y)  { return 1;  }
    return 0;
}

int main () {
   int n;

   printf("Before sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%f ", values[n]);
   }

   qsort(values, 5, sizeof(double), compare_doubles);

   printf("\nAfter sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {   
      printf("%f ", values[n]);
   }
  
   return(0);
}
