#include <iostream>

int main() {
    double a,b;
    std::cout.precision(10);
    std::cout << std::fixed;

    std::cin >> a >> b;
    std::cout << a/b;
}