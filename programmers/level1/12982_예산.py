def solution(d, budget):
    answer = 0
    # 최대한 많은 팀에 배분해야하므로
    # 가장 적은 예산을 필요로 하는 팀부터 오름차순으로 정렬
    d.sort()

    for i in d:
        # 예산이 허용하는 한 지원
        if budget >= i:
            budget -= i
            answer += 1
        # 예산이 요청 금액보다 많을 경우 중단
        else:
            break

    return answer


"""
정답확인용 테스트 케이스
print((solution([1,3,2,5,4], 9)))  #3
print((solution([2,2,3,3], 10)))   #4
"""

1, 2, 3, 4, 5