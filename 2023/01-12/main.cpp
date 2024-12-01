#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include "../main.hpp"

using std::cout, std::cin, std::endl, std::string;

int main() {

    file myfile("input.txt");
    if (!myfile) {
        std::cerr << "Input file cannot be opened for reading.\n";

        return 1;
    }
    int sum{0};

    while (myfile.getfile()) {
        string line;
        myfile.getfile() >> line;
        if (line.empty()) {
            break;
        }
        string strnum;
        strnum.push_back(*std::find_if(line.begin(), line.end(),
                                       [](char c) { return isdigit(c); }));
        strnum.push_back(*std::find_if(line.rbegin(), line.rend(),
                                       [](char c) { return isdigit(c); }));
        sum += std::stoi(strnum);
    }
    std::cout << sum << "\n";
    return 0;
}
