#include <vector>
#include <string>

namespace veclib {
    template <class CType>
    CType sum_vec(std::vector<CType> & vec) {
        CType rez = 0;
        for (auto& v : vec) { rez += v; }
        return rez;
    }

    template <class CType>
    CType prod_vec(std::vector<CType> & vec) {
        CType rez = 1;
        for (auto& v : vec) { rez *= v; }
        return rez;
    }


    template <class CType>
    CType dot_vec(std::vector<CType> & vec1, std::vector<CType> & vec2) {
        CType rez = 0;
        for (uint i = 0; i < vec1.size(); i++) { rez += vec1[i] * vec2[i]; }
        return rez;
    }


    template <class CType>
    std::string str_vec(std::vector<CType> & vec) {
        std::string rez("[");
        for (auto && elem : vec) { rez += std::to_string(elem) + " "; }
        rez[rez.size()-1] = ']';
        return rez;
    }
}
