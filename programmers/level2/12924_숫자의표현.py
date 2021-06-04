def solution(n):
    answer = 0

    # 1부터 연속된 수를 더하기
    for i in range(1, n + 1):
        temp = 0
        for j in range(i, n + 1):
            temp += j
            # 더한 수가 n과 같다면 정답에 추가하고 다음번 째 수부터 연속된 수를 더하기
            if temp == n:
                answer += 1
                break
            # 연속된 수를 더하다가 n보다 커지면 중단하고 다음번 째 수부터 연속된 수를 더하기
            elif temp > n:
                break

    return answer