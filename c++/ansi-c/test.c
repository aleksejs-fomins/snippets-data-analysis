/* rand example: guess the number */
#include <stdio.h>     
#include <string.h>     /* memcpy */
#include <stdlib.h>     /* qsort, srand, rand */
#include <time.h>       /* time */
#include <assert.h>
#include <math.h>

typedef unsigned int uint;

extern void arr_diff_1D(uint size, const double a1[size], const double a2[size], double rez[size]);
extern void arr_sum_1D(uint size, const double a1[size], const double a2[size], double rez[size]);
extern void arr_scale_1D(uint size, const double a1[size], double alpha, double rez[size]);
extern double arr_l2norm_1D(uint size, double a1[size]);
extern void arr_urand_2D(uint nRows, uint nCols, double rez[nRows][nCols], double l, double r);
extern void all_k_nearest_neighbors(uint nData, uint nDim, uint k, const double data[nData][nDim], double rez[nData][k]);



double urand(double l, double r)  { return l + r * ((double)rand() / (double)RAND_MAX); }

void arr_diff_1D(uint size, const double a1[size], const double a2[size], double rez[size]) {
    for (uint i=0; i < size; i++)  { rez[i] = a1[i] - a2[i]; }
}

void arr_sum_1D(uint size, const double a1[size], const double a2[size], double rez[size]) {
    for (uint i=0; i < size; i++)  { rez[i] = a1[i] + a2[i]; }
}

void arr_scale_1D(uint size, const double a1[size], double alpha, double rez[size]) {
    for (uint i=0; i < size; i++)  { rez[i] = alpha * a1[i]; }
}

double arr_l2norm_1D(uint size, double a1[size]) {
    double rez = 0;
    for (uint i=0; i < size; i++)  { rez += a1[i]*a1[i]; } 
    return sqrt(rez);
}

void arr_urand_2D(uint nRows, uint nCols, double rez[nRows][nCols], double l, double r) {
    for (uint i = 0; i < nRows; i++)  {
        for (uint j = 0; j < nCols; j++)  {
            rez[i][j] = urand(l, r);
        }
    }
}

int compare_doubles(const void *a, const void *b) {
    double *x = (double *) a;
    double *y = (double *) b;
    if      (*x < *y)  { return -1; }
    else if (*x > *y)  { return 1;  }
    return 0;
}

void all_k_nearest_neighbors(uint nData, uint nDim, uint k, const double data[nData][nDim], double rez[nData][k]) {
    double *diff  = malloc(nDim * sizeof(double));
    double *dists = malloc(nData * sizeof(double));
    
    for (uint i = 0; i < nData; i++) {
        
        // 1. Evaluate distance between every pair of points
        for (uint j = 0; j < nData; j++) {
            arr_diff_1D(nDim, data[i], data[j], diff);
            dists[j] = arr_l2norm_1D(nDim, diff);
        }
        
        // 2. For every point, sort distances in ascending order
        qsort(dists, nData, sizeof(double), compare_doubles);
        
        
        // 3. Return slice of sorted array
        memcpy(&rez[i], dists + 1, k * sizeof(double));
    }
    
    free(diff);
    free(dists);
}


int main() {
    srand(time(NULL));
    
    const uint N_DATA = 1000;
    const uint N_DIM = 3;
    const uint K = 2;
    
    // Initialize data with uniform random numbers
    double data[N_DATA][N_DIM];
    arr_urand_2D(N_DATA, N_DIM, data, 0, 1);
    
    // Compute nearest neighbors
    double aknn[N_DATA][K];
    all_k_nearest_neighbors(N_DATA, N_DIM, K, data, aknn);
    
    for (uint iK = 0; iK < K; iK++) {
        for (uint iData = 0; iData < N_DATA; iData++) {
            printf("%f ", aknn[iData][iK]);
        }
        printf("\n");
    }
    
    return 0;
}
