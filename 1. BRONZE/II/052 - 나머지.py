num = []
for _ in range(10):
    num.append(int(input()))

R = []
for i in range(10):
    R.append(num[i]%42)

print(len(set(R)))