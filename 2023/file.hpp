#pragma once
#include <fstream>
#include <iostream>

class file {
  public:
    std::string name;
    std::ifstream filename; // Declare filename as a member variable

  public:
    explicit file(const std::string name) : name(name) {
        this->filename.open(name); // Initialize filename in the constructor
    }
    virtual ~file() { this->filename.close(); }
    bool is_file_opened() { return (this->filename.is_open()); }
    bool operator!() { return !this->is_file_opened(); }
    std::ifstream& getfile() {
        return this->filename;
    } // Return a reference to filename
};
