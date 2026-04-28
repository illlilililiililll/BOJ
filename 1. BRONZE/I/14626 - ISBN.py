ISBN = input()

total = 0
weight = 1
for i in range(13):
    if ISBN[i] == '*':
        if i % 2 != 0:
            weight = 3
        continue
    
    if i % 2 == 0:
        total += int(ISBN[i])
    else:
        total += 3 * int(ISBN[i])

for i in range(10):
    if (total + i * weight) % 10 == 0:
        print(i)
        break