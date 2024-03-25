def pal(word):
    if len(word) <= 1:
        print('yes')
        return
    if word[0] == word[-1]:
        return pal(word[1:-1])
    else:
        print('no')
        return

while True:
    word = input()
    if word == '0':
        break
    pal(word)