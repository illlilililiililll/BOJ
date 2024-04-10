#include <iostream>

int main() {
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int n, v;
    std::cin >> n;

    int a[n];

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::cin >> v;

    int count = 0;
    for (auto i : a) {
        if (i == v)
            count += 1;
    }

    std::cout << count;

    return 0;
}