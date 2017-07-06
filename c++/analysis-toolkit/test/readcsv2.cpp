#include<iostream>
#include<fstream>
#include<assert.h>
#include<vector>
#include<string>

#include "../readcsv.hh"

typedef CSVParser::StrVec     StrVec;
typedef CSVParser::StrVecVec  StrVecVec;

int main(int argc, char** argv) {
    assert(argc == 2);
    
    //typedef std::string ctype;
    //typedef int ctype;
    //typedef float ctype;
    typedef double ctype;
    std::vector<ctype> datacol = CSVParser::readcsvcol<ctype>(argv[1], "|", 1);

    for (size_t i = 0; i < datacol.size(); i++) {
        std::cout << datacol[i] << std::endl;
    }
    
    return 0;
}