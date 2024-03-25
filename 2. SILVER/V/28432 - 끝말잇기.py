import sys
input = sys.stdin.readline

N = int(input())
N_list = []

for i in range(N):
    N_list.append(input().strip())
where = N_list.index('?')

if where == 0:
    if N != 1:
        end = N_list[where+1][0] 
        flag = 'end'
    else:
        flag = 'odd' 
elif where == N-1:
    first = N_list[where-1][-1]
    flag = 'first' 
else:
    first = N_list[where-1][-1] 
    end = N_list[where+1][0]
    flag = 'mid'

N_set = set(N_list)

M = set()
for j in range(int(input())):
    M.add(input().strip())
M = list(M - N_set)

for i in M:
    if flag == 'first':
        if i[0] == first:
            print(i)
            break
    elif flag == 'end':
        if i[-1] == end:
            print(i)
            break
    elif flag == 'mid':
        if i[0] == first and i[-1] == end:
            print(i)
            break
    elif flag == 'odd':
        print(i)
        break
