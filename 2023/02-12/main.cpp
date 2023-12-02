#include <fstream>
#include <functional>
#include <iostream>
#include <string>

using std::cout, std::cin, std::endl, std::string;

int main() {

    std::ifstream myfile("input.txt");

    if (!myfile) {
        std::cerr << "Input file cannot be opened for reading.\n";

        return 1;
    }

    while (myfile) {
        string line;
        std::getline(myfile, line);
        if (line.empty()) {
            break;
        }
        cout << line << "\n";
    }
    myfile.close();

    return 0;
}
