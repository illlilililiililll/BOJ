for _ in range(int(input())):
    answer = input()
    score = 0
    now_score = 1
    for i in range(len(answer)):
        if answer[i] == 'O':
            score += now_score
            now_score += 1
        else:
            now_score = 1
    print(score)