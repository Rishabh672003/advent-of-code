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
    int sum{0};

    while (myfile) {
        string line;
        myfile >> line;
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

    myfile.close();
    return 0;
}
