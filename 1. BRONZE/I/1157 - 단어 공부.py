word = list(input().upper())
count = []

letter = list(set(word))
for i in letter:
    count.append(word.count(i))

if count.count(max(count)) > 1:
    print('?')
else:
    print(letter[count.index(max(count))])