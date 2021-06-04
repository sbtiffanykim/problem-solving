def solution(A, B):
    answer = 0

    # 곱하여 더한 값이 최솟값
    # 한쪽에는 남아있는 수 중 가장 큰 수, 한쪽에서는 가장 작은 수를 곱하여 더해야 한다
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer