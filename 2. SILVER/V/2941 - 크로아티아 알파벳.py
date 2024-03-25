n = input()

if 'c=' in n:
    n = n.replace('c=', 'c')
if 'c-' in n:
    n = n.replace('c-', 'c')
if 'dz=' in n:
    n = n.replace('dz=', 'd')
if 'd-' in n:
    n = n.replace('d-', 'd')
if 'lj' in n:
    n = n.replace('lj', 'l')
if 'nj' in n:
    n = n.replace('nj', 'n')
if 's=' in n:
    n = n.replace('s=', 's')
if 'z=' in n:
    n = n.replace('z=', 'z')

print(len(n))