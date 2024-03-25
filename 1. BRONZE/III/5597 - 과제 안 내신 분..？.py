n = []
for i in range(1, 31):
    n.append(i)
    
for _ in range(28):
    n.remove(int(input()))
    
print(n[0])
print(n[1])