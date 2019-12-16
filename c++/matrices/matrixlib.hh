#include <iostream>
#include <vector>
#include <string>

#include "randlib.hh"
#include "veclib.hh"

namespace matrixlib {
    
    typedef std::vector<uint> IntVec1D;

    template <class CType>
    class Matrix {
    public:
        typedef std::vector<CType> DataVec1D;

    private:
        IntVec1D dim;
        IntVec1D dimIncr;
        DataVec1D data1D;
        
    public:

        Matrix(IntVec1D & dimThis) {
            dim = dimThis;
            uint size = veclib::prod_vec(dim);
            data1D = DataVec1D(size, 0);
            
            dimIncr = IntVec1D(dim.size(), 1);
            for (int i = dim.size() - 2; i >= 0; i--) {
                dimIncr[i] = dimIncr[i+1] * dim[i+1];
            }
        }

        
        uint size_1D() { return data1D.size(); }
        
        
        void reinit_urand(CType l, CType r) {
            for (uint i = 0; i < data1D.size(); i++) {
                data1D[i] = randlib::urand(l, r);
            }
        }
    
    
        IntVec1D index_from_1D(uint idx1D) {
            IntVec1D rez(dim.size(), 0);
            for (uint i = 0; i < dimIncr.size(); i++) {
                rez[i] = idx1D / dimIncr[i];
                idx1D = idx1D % dimIncr[i];
            }
            return rez;
        }


        uint index_to_1D(IntVec1D & idxVec) {
            return veclib::dot_vec(idxVec, dimIncr);
        }

        
        std::string to_string() {
            std::cout << veclib::str_vec(dimIncr) << std::endl;
            
            std::string rez("---" + std::to_string(dim.size()) + "D matrix of dimensions " + veclib::str_vec(dimIncr) + "---\n");
            for (uint i = 0; i < data1D.size(); i++) {
                IntVec1D idx = index_from_1D(i);
                rez += veclib::str_vec(idx) + " " + std::to_string(data1D[i]) + "\n";
            }
            rez += "---End Matrix---\n";
            return rez;
        }
    };
    
}
