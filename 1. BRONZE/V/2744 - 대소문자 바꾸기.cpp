#include <iostream>

int main() {
    std::string a;
    std::cin >> a;

    for(char &i : a) {
        if (i >= 90)
            i -= 32;
        else    
            i += 32;
    }

    std::cout << a;

    return 0;
}