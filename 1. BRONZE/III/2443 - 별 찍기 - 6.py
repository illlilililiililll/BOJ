n = int(input())

for i in range(n, 0, -1):
    star = 2*i-1
    print(' '*int(((2*n-1-star)/2))+'*'*star)