def is_vps(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif not stack:
            return False
        else:
            stack.pop()
    return not stack

for _ in range(int(input())):
    print('YES' if is_vps(input()) else 'NO')