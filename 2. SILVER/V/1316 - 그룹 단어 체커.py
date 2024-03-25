import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    letters = set()
    word = input().strip()
    for i in range(len(word)):
        if word[i] not in letters:
            letters.add(word[i])
        elif word[i] in letters and word[i-1] == word[i]:
            continue
        else:
            break
    else:
        count += 1

print(count)