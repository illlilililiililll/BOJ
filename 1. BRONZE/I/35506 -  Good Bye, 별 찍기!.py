n = int(input())

for i in range(n, 0, -1):
    print(format((n + i - 1) * ' ' + '*' + n * ' ' + '*' + (2 * (n - i) + 1) * ' '+ '*', f'{4*n+2}'))

for i in range(n-1, -1, -1):
    print(format(i * ' ' + '*' + (2 * (n - i) + n - 1) * ' ' + '*' + (2 * i + 1) * ' ' + '*', f'{4*n+2}'))