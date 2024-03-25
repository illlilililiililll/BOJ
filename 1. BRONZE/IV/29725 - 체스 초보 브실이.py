import sys
input = sys.stdin.readline
def score(letter:str):
    letter = letter.lower()  # 소문자로 변환한 결과를 변수에 저장
    if letter == 'k':
        return 0
    elif letter == 'p':
        return 1
    elif letter == 'n' or letter == 'b':
        return 3
    elif letter == 'r':
        return 5
    elif letter == 'q':
        return 9
chess = []
for _ in range(8):
    chess.append(input())
total = 0
for i in range(8):
    for j in range(8):
        unit = chess[i][j]
        if unit != '.':
            if unit.isupper():
                total += score(unit)
            else:
                total -= score(unit)
print(total)