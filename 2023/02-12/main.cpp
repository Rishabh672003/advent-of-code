#include "../file.hpp"
#include <fstream>
#include <functional>
#include <iostream>
#include <string>

using std::cout, std::cin, std::endl, std::string;

int main() {

    file myfile("input.txt");

    if (!myfile) {
        std::cerr << "Input file cannot be opened for reading.\n";

        return 1;
    }

    while (!myfile.getfile().eof()) {
        string line;
        std::getline(myfile.getfile(), line);
        if (line.empty()) {
            break;
        }
        cout << line << "\n";
    }
    int* a = *int(malloc(sizeof(int)));

    return 0;
}
