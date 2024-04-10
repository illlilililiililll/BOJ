#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int result = 1;
    for (int i = 1; i < n+1; i++)
        result *= i;
    
    std::cout << result;

    return 0;
}