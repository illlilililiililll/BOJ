n = int(input())

for i in range(1, n+1):
    py = 2*i-1
    if i == 1:
        print(' '*int(((2*n-1-py)/2))+'*')
    else:
        print(' '*int(((2*n-1-py)/2))+'*'+' '*(py-2)+'*')