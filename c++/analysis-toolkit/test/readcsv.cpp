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
    
    StrVecVec dataset = CSVParser::readcsv(argv[1], "|");
    
    for (size_t i = 0; i < dataset.size(); i++) {
        std::cout << "c" << i << " ::: ";
        for (size_t j = 0; j < dataset[i].size(); j++) {
            std::cout << dataset[i][j] << ";";
        }
        std::cout << std::endl;
    }
    
    return 0;
}