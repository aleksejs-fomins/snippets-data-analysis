#include <stdlib.h>     /* srand, rand */

namespace randlib {
    // Uniform random number
    template <class CType>
    CType urand(CType l, CType r) { return l + r * ((double)rand() / (double)RAND_MAX); }
}
