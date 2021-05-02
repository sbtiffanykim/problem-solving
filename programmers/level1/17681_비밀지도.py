"""
#17681: 비밀지도
"""


def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        # 0b-형태의 이진수로 나타냄
        # 둘 다 벽일 경우에 벽(1), 아니라면 공백(0)으로 나타내기 위해 or연산 씀
        t = bin(i | j)
        # '0b' 없애기
        t = t[2:]
        # 자릿수를 맞추기 위해 n자리로 표시하고, 못채운 부분을 0으로 표시
        t = t.rjust(n, "0")
        t = t.replace("0", " ")
        t = t.replace("1", "#")
        answer.append(t)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))