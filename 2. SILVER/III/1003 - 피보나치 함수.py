n = int(input())

total = [(1, 0), (0, 1)]
for _ in range(n):
    a = int(input())

    while len(total) < a + 1:
        l = len(total)
        total.append((total[l-1][0] + total[l-2][0], total[l-1][1] + total[l-2][1]))
    
    print(total[a][0], total[a][1])