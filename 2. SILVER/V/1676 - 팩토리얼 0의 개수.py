n = int(input())
fact = 1
for _ in range(1, n+1):
    fact *= _

fact = str(fact)

count = 0
for i in range(len(fact)):
    if fact[-1-i] == '0':
        count += 1
    else:
        break

print(count)