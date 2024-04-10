#include <iostream>

int main() {
    int year;
    std::cin >> year;

    int result = (year % 4 == 0 ? ((year % 400 != 0) && (year % 100 == 0) ? 0 : 1) : 0);

//    if (year % 4 == 0)
//        if ((year % 100 == 0) && (year % 400 != 0))
//            result = 0;
//        else
//            result = 1;
//    else
//        result = 0;
//    (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0))

    std::cout << result;

    return 0;
}