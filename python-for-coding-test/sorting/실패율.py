def solution(N, stages):
    answer = []
    # 실패율을 저장할 배열
    rate = []

    # stage마다 반복
    for i in range(1, N + 1):
        participants = 0  # 각 스테이지에 참가한 사람을 저장할 변수
        fail = 0  # 클리어하지 못한 사람을 저장할 변수

        for s in stages:
            # 입력된 리스트에서 i보다 같거나 크면 i번째 스테이지에 도달한 플레이어임
            if s >= i:
                participants += 1
            # 입력된 리스트에서 i보다 같으면 i번째 스테이지를 시도중이므로 클리어하지는 않았음
            # i보다 작은 사람은 i번째 스테이지에 도달하지 못했으므로 처리하지 않음
            if s == i:
                fail += 1
        # i번째 스테이지에 도달한 사람이 없으면 실패율은 0이다
        if participants == 0:
            rate.append((i, 0))
        else:
            rate.append((i, (fail / participants)))

    # 실패율을 기준으로 내림차순 정렬
    rate.sort(reverse=True, key=lambda x: x[1])

    for i in range(N):
        answer.append(rate[i][0])

    return answer


"""정답 확인용 테스트케이스"""
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4]))