#ifndef TOOLKIT_READCSV_HH
#define TOOLKIT_READCSV_HH

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<assert.h>

namespace CSVParser {
    typedef std::vector<std::string>  StrVec;
    typedef std::vector<StrVec>       StrVecVec;

    // Overload conversion of a string into other types
    //std::string strconv(const std::string & str) { return str; }
    //int strconv(const std::string & str) { return std::stoi(str); }
    //float strconv(const std::string & str) { return std::stof(str); }
    //double strconv(const std::string & str) { return std::stod(str); }

    template<typename T>
    T strconv(const std::string & str) { }
    
    template<>
    std::string strconv<std::string>(const std::string & str) { return str; }

    template<>
    int strconv<int>(const std::string & str) { return std::stoi(str); }
    
    template<>
    float strconv<float>(const std::string & str) { return std::stof(str); }
    
    template<>
    double strconv<double>(const std::string & str) { return std::stod(str); }
    
    
    
    // Separate a string into chunks using a delimiter
    StrVec parsestr(std::string str, std::string sep) {
        StrVec rez;
        size_t pos = 0;
        while ((pos = str.find(sep)) != std::string::npos) {
            rez.push_back(str.substr(0, pos));
            str.erase(0, pos + sep.length());
        }
        rez.push_back(str);
        return rez;
    }

    
    // Read a CSV file into a vector of vectors of strings
    StrVecVec readcsv(std::string filename, std::string sep) {
        StrVecVec rez;
        
        std::ifstream infile;
        infile.open(filename.c_str());
        
        std::string line;
        while (std::getline(infile, line)) {
            rez.push_back(parsestr(line, sep));
        }
        infile.close();
        
        return rez;
    }
    
    
    // Extract a given column from a file, and convert it into a given type
    template <class ctype>
    std::vector<ctype> readcsvcol(std::string filename, std::string sep, size_t col) {
        std::vector<ctype> rez;
        
        std::ifstream infile;
        infile.open(filename.c_str());
        
        std::string line;
        while (std::getline(infile, line)) {
            StrVec list = parsestr(line, sep);
            assert(col < list.size());
            rez.push_back(strconv<ctype>(list[col]));
        }
        infile.close();
        
        return rez;
    }
}



#endif //TOOLKIT_READCSV_HH