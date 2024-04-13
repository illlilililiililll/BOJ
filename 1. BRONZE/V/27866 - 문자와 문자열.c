#include <stdio.h>

int main() {
    char a[1000];
    scanf("%s", a);

    int n;
    scanf("%d", &n);

    printf("%c", a[n-1]);

    return 0;
}