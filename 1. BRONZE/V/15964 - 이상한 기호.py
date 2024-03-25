a, b = map(int, input().split())
print((lambda a, b : (a+b)*(a-b))(a, b))