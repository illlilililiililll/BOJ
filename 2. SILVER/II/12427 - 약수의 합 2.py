import sys
input = sys.stdin.readline

def Div(n):
    div = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
    
    return sum(div)

n = int(input())

result = 0
for i in range(1, n+1):
    result += (n//i)*i

print(result)