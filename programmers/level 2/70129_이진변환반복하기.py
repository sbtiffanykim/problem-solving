def solution(s):
    answer = []

    zeros = 0
    res = 0
    while s != "1":
        zeros += s.count("0")
        # 0을 제거한 string
        temp_str = "".join(filter(lambda x: x == "1", s))
        l = len(temp_str)
        s = bin(l)[2:]
        res += 1

    answer.append(res)
    answer.append(zeros)

    return answer


# 더 좋은 방법이 같은제목2에 있음
# 0을 제외한 str의 길이를 구하고 2진수로 바꾸기 때문에 실제 1차 변환한 str을 구할 필요가 없음

"""
print((solution("110010101001")))  # [3, 8]
print((solution("01110")))  # [3, 3]
print((solution("1111111")))  # [4, 1]
"""