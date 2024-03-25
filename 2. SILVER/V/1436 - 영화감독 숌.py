n = int(input())

num = []

i = 0
while True:
    if len(num) == n:
        break
    w = str(i)
    if '666' in w:
        num.append(w)
    i += 1

print(num[n-1])