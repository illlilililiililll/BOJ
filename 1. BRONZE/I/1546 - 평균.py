n = int(input())
score = list(map(int, input().split()))

high = max(score)

new_score = []
for i in range(n):
    new_score.append(score[i]/high*100)

print(sum(new_score)/n)