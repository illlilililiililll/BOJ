import sys
input = sys.stdin.readline
n = input().strip()
c=0
while len(n)>=2:
    t = 0
    for i in n:
        t+=int(i)
    n=str(t)
    c+=1
print(c)
if int(n)%3==0:
    print("YES")
else:   
    print('NO')