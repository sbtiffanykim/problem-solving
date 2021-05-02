"""
#12948: 핸드폰 번호 가리기
"""


def solution(phone_number):
    answer = ""

    n = len(phone_number)
    t = "*" * (n - 4) + phone_number[-4:]
    answer = t

    return answer