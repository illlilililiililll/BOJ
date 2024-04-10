#include <iostream>

using namespace std;

int main() {
    cout << fixed;
    cout.precision(1);

    string score;
    cin >> score;

    float point = 0.0;

    switch (score[0]) {
        case 'A':
            point += 4.0;
            break;
        case 'B':
            point += 3.0;
            break;
        case 'C':
            point += 2.0;
            break;
        case 'D':
            point += 1.0;
            break;
    }

    switch (score[1]) {
        case '+':
            point += 0.3;
            break;
        case '-':
            point -= 0.3;
            break;
    }

    cout << point;

    return 0;
}