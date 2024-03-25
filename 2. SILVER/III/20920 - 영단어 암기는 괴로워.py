import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    words.append(word)

word_list = sorted(Counter(words).most_common(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for _ in word_list:
    print(_[0])