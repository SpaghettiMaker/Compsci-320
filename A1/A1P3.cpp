#include <iostream>
#include <string>
#include <sstream>
#include <array>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

std::string emulti(std::vector<int> baseVector) {
    int count = 0;
    int index = 2;
    std::string result = "";

    while (index < 169) {
        count = std::count(baseVector.begin(), baseVector.end(), index);
        if (count > 1) {
            if (result.length() >= 1) {
                result += "*";
            }
            result += std::to_string(index) + "^" + std::to_string(count);
        }
        if (count == 1) {
            if (result.length() >= 1) {
                result += "*";
            }
            result += std::to_string(index);
        }
        ++index;
    }

    for (int &baseValue : baseVector) {
        if (baseValue == 0) {
            result = "0";
            break;
        }
        if (baseValue == 1 && result.length() < 1) {
            result = "1";
        }
    }
    
    return result;
}

int main() {
    int check = 0;
    int base = 0;
    int power = 0;
    int num = 1;
    int tempInt = 0;
    std::string input;
    std::string tempSting;
    std::vector<int> baseVector;
    // dont use pfe as large number have multiple primes as factors
    getline(cin, input);

    for (char &c : input) {
        if (c == ' ' || c == '*') {
            if (check == 1) {
                if (base > 0) {
                    tempInt = std::stoi(tempSting, nullptr);
                    while (tempInt > 0) {
                        baseVector.push_back(base);
                        --tempInt;
                    }
                    base = 0;
                } else {
                    tempInt = std::stoi(tempSting, nullptr);
                    baseVector.push_back(tempInt);
                }
                check = 0;
                tempSting = "";
            }
            
        } else if (c == '^') {
            base = std::stoi(tempSting, nullptr);
            tempSting = "";
        } else {
            tempSting += c;
            check = 1; 
        }
    }
    if (tempSting.length() >= 1) {
        if (base > 0) {
            tempInt = std::stoi(tempSting, nullptr);
            while (tempInt > 0) {
                baseVector.push_back(base);
                --tempInt;
            }
            base = 0;
        } else {
            tempInt = std::stoi(tempSting, nullptr);
            baseVector.push_back(tempInt);
        }
    }

    std::cout << emulti(baseVector) << endl;

    /*for(int &baseValue : baseVector) {
        std::cout << baseValue << std::endl;
    }*/
    

    
    return 0;
}

