n = int(input())

for i in range(n):
    num = 0
    full = list(map(int, input().split()))
    case = int(full[0])
    av = (sum(full[1:])) / case
    for j in range(1, case+1):
        if full[j] > av:
            num += 1
    print(str(round(num/case*100, 3)) + '%')