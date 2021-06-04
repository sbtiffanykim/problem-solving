def solution(n):
    answer = 0
    # 주어진 n을 이진수로 변환
    bin_num = bin(n)[2:]
    # 1의 개수를 저장
    count_ones = bin_num.count("1")

    # n을 1씩 증가시킨 수를 2진수로 변환했을 때
    num = n + 1
    while True:
        # 1의 개수가 count_ones와 같으면
        if bin(num)[2:].count("1") == count_ones:
            # 정답이 됨
            answer = int(num)
            break
        num += 1

    return answer


"""
print(solution(78))  # 83
print(solution(15))  # 23
"""