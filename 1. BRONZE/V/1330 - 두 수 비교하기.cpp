#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;

    std::string result;

    if (a > b)
        result = ">";
    else if (a < b)
        result = "<";
    else
        result = "==";

    std::cout << result;

    return 0;
}