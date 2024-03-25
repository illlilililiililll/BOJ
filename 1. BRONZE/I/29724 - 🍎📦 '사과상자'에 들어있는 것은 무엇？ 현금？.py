import sys
input = sys.stdin.readline

mass = 0
price = 0
for _ in range(int(input())):
    t, w, h, l = map(lambda x: int(x) if x.isdigit() else x, input().split())
    if t == 'B':
        mass += 6000
    elif t == 'A':
        width = w//12
        height = h//12
        length = l//12
        apple = width*length*height
        mass += 1000+500*apple
        price += apple*4000

print(mass, price, sep='\n')