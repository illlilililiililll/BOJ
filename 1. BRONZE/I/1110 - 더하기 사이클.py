n = input()

def digit_sum(n):
    n = list(n)
    result = 0
    for i in n:
        result += int(i)
    return str(result)

count = 0
goal = int(n)

while True:
    count += 1
    if int(n) < 10:
        n = '0' + n
    n = n[-1] + digit_sum(n)[-1]
    # print(n)
    if int(n) == goal:
        break

print(count)