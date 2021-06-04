def solution(s):

    zeros = 0
    res = 0
    while s != "1":
        res += 1
        zeros += s.count("0")
        # 0을 제외한 후 길이
        t = len(s) - s.count("0")
        # 길이를 이진법으로 변환
        s = bin(t)[2:]

    return [res, zeros]


"""
print((solution("110010101001")))  # [3, 8]
print((solution("01110")))  # [3, 3]
print((solution("1111111")))  # [4, 1]
"""