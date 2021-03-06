#include <iostream>
#include <string>
#include <sstream>
#include <array>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

std::string pfe(int num, std::vector<int> primeVector) {
    int index = 2;
    int count = 0;
    std::string result = "";

    if (num == 1) {
        return "1";
    }
    if (num == 0) {
        return "0";
    }

    for(int &primeValue : primeVector) {
        count = 0;
        if (num == 1) {
            break;
        }
        while (num % primeValue == 0 && num != 1) {
            count++;
            num = num / primeValue;
        }
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
        index++;
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


    getline(cin, input);
    std::vector<int> primeVector = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
        79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
        197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 
        461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 
        607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 
        751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 
        907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};

    for (char &c : input) {
        if (c == ' ' || c == '*') {
            if (check == 1) {
                if (base > 0) {
                    base = pow(base, std::stoi(tempSting, nullptr));
                    num *= base;
                    base = 0;
                } else {
                    tempInt = std::stoi(tempSting, nullptr);
                    if (tempInt < 2) {
                        num *= tempInt;
                    } else {
                        num *= primeVector[tempInt - 2];
                    }
                }
            tempSting = "";
            }
        } else if (c == '^') {
            base = primeVector[std::stoi(tempSting, nullptr) - 2];
            tempSting = "";
        } else {
            tempSting += c;
            check = 1; 
        }
    }
            if (check == 1) {
                if (base > 0) {
                    base = pow(base, std::stoi(tempSting, nullptr));
                    num *= base;
                    base = 0;
                } else {
                    tempInt = std::stoi(tempSting, nullptr);
                    if (tempInt < 2) {
                        num *= tempInt;
                    } else {
                        num *= primeVector[tempInt - 2];
                    }
                }
            tempSting = "";
            }

    
    std::cout << pfe(num, primeVector) << std::endl;

    
    return 0;
}

