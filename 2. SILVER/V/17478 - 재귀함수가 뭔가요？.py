def chatbot_recursive(N, depth):
    # 들여쓰기를 만들기 위한 공백 생성
    indent = "____" * depth

    # 기저 사례: N이 0이면 더 이상 재귀 호출하지 않음
    if N == 0:
        return
    print(f"{indent}\"재귀함수가 뭔가요?\"")
    # 챗봇의 응답 출력
    if N == 1:
        print(f"{indent}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    else:
        print(f"{indent}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(f"{indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(f"{indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")

    # 재귀 호출
    chatbot_recursive(N - 1, depth + 1)

    # 챗봇의 답변 출력
    print(f"{indent}라고 답변하였지.")

# 입력 받기
N = int(input())

# 챗봇 응답 시작
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot_recursive(N+1, 0)