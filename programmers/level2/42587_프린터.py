def solution(priorities, location):
    answer = 0
    # 가장 우선순위가 높은 것을 찾기
    max_p = max(priorities)

    while True:
        # 프린터 대기 목록을 순회하면서 확인
        for i in range(len(priorities)):
            # 가장 우선순위에 있는 작업과 현재 작업의 우선순위가 같다면
            if max_p == priorities[i]:
                # 인쇄된 것으로 간주
                answer += 1
                # 인쇄된 작업의 우선순위는 0으로 변경(고려 안되게 제외)
                priorities[i] = 0
                # 그 다음으로 큰 우선순위를 확인
                max_p = max(priorities)
                # 만약 현재 인쇄중인 작업과 요청한 문서가 같을 경우
                if i == location:
                    # 종료 후 정답 출력
                    return answer


"""
print(solution([2, 1, 3, 2], 2))   # 1
print(solution([1, 1, 9, 1, 1, 1], 0))   # 5
"""