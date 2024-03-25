import sys
from collections import Counter
input = sys.stdin.readline

book = []
for _ in range(int(input())):
    book.append(input().strip())

count = sorted(Counter(book).most_common(), key=lambda x:(-x[1], x[0]))
print(count[0][0])