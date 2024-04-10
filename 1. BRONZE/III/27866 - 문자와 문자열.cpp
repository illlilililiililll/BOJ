#include <iostream>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string a;
    while (true) {
        std::getline(std::cin, a);
        if (a == "")
            break;

        std::cout << a << '\n';
    }

    return 0;
}