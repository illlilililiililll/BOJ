n = int(input())

last = 1
for i in range(1, n+1):
    last *= i

last = str(last)
print(last.strip('0')[-1])