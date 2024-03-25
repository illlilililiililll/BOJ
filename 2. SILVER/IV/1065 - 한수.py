n = int(input())

count = 0
for i in range(1, n+1):
    j = str(i)
    if len(j) <= 2:
        count += 1
        continue
    elif j == '1000':
        continue
    if int(j[0]) + int(j[-1]) == 2*int(j[1]):
        count += 1
print(count)