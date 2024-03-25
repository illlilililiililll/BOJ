num = set(i for i in range(1, 10001))
notSelf = set()

for n in num:
    add = n
    for i in str(n):
        add += int(i)
    notSelf.add(add)
num -= notSelf
num = sorted(num)
for _ in num:
    print(_)