n = int(input())

for _ in range(n):
    time, string = input().split()
    result = ''
    for i in range(len(string)):
        result += string[i]*int(time)
    print(result)