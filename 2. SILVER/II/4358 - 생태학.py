import sys
input = sys.stdin.readline

trees = dict()
n = 0
while True:
    tree = input().strip()
    if not tree:
        break
    n += 1
    if tree not in trees.keys():
        trees[tree] = 1
    else:
        trees[tree] += 1

trees = dict(sorted(trees.items()))
for i in trees:
    print('%s %.4f' %(i, (trees[i]/n)*100))