import sys
input = sys.stdin.readline

for i in range(1, int(input())+1):
    all = list(map(int, input().split()))
    students = sorted(all[1:])
    maxdiff = -1
    for j in range(len(students)-1):
        diff = students[j+1] - students[j]
        if diff > maxdiff:
            maxdiff = diff
    print(f'Class {i}\nMax {max(students)}, Min {min(students)}, Largest gap {maxdiff}')