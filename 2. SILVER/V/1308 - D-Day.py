import datetime

y, m, d = map(int, input().split())
yx, mx, dx = map(int, input().split())
now = datetime.date(y, m, d)
exit = datetime.date(y+1000, m, d)
end = datetime.date(yx, mx, dx)

if end >= exit:
    print('gg')
else:
    print(f"D-{(end-now).days}")