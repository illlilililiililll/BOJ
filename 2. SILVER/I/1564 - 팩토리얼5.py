n = int(input())

result = 1

for i in range(1, n+1):
    result *= i     
    result = int(str(result).rstrip('0')[-12:])

print(str(result)[-5])