/* rand example: guess the number */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <assert.h>

#include <iostream>

#include "matrixlib.hh"

int main()
{
    srand(time(NULL)); // randomize seed
    
    matrixlib::IntVec1D shape = {2, 3, 4};
    matrixlib::Matrix<double> M1(shape);
    
    //Test 1: check that 1D and ND indices are consistent
    for (uint idx1D = 0; idx1D < M1.size_1D(); idx1D++) {
        matrixlib::IntVec1D idx = M1.index_from_1D(idx1D);
        assert(idx1D == M1.index_to_1D(idx));
    }   
    
    //Test 2: fill matrix with random numbers and print it
    M1.reinit_urand(0, 1);
    std::cout << M1.to_string() << std::endl;
    
    return 0;
}
