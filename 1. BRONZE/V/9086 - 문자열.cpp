#include <iostream>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::string a;
    for (int i = 0; i < n; i++) {
        std::cin >> a;
        std::cout << a[0] << a[a.length()-1] << '\n';    }

    return 0;
}