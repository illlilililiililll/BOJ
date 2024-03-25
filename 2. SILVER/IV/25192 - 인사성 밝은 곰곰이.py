import sys
input = sys.stdin.readline

gomgom = 0
log = set()
for _ in range(int(input())):
    chat = input().strip()
    if chat == 'ENTER':
        log.clear()
        continue
    if chat not in log:
        gomgom += 1
        log.add(chat)
    
print(gomgom)