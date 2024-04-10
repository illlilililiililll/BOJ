#include <iostream>

int main() {
    int result = 0;
    int n;
    for (int i = 0; i < 5; i++) {
        std::cin >> n;
        result += n*n;
    }

    std::cout << result%10;
    
    return 0;
}