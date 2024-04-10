#include <iostream>

int main() {
    int a[30] = {0, };

    int n;
    for (int i = 0; i < 28; i++) {
        std::cin >> n;
        a[n-1] = 1;
    }

    for (int i = 0; i < 30; i++) {
        if (!a[i])
            std::cout << i+1 << '\n';
    }

    return 0;
}