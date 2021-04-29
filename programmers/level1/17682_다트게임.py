"""
#17682: 다트게임
"""

import re


def solution(dartResult):
    answer = 0
    # 각 세트에서 얻은 점수를 저장하기 위한 배열 초기화
    scores = []

    # 점수|보너스|[옵션]의 3세트로 나누기
    darts = re.findall("(\d{0,10}[S|D|T][*]*#*)", dartResult)

    # 각 세트마다 수행
    for d in range(3):
        # 세트에서 얻은 점수 저장
        score = 0
        # str을 int로 바꿀 때에 사용
        temp = ""

        # 각 단위별로 자르기
        for i in range(len(darts[d])):
            # 0-10까지 확인
            if darts[d][i].isdigit():
                temp += darts[d][i]
        # 숫자부분 처리
        score += int(temp)

        # 보너스 처리
        if "D" in darts[d]:
            score = score ** 2
        elif "T" in darts[d]:
            score = score ** 3

        # 옵션 처리
        if "#" in darts[d]:
            score *= -1

        if "*" in darts[d]:
            if d != 0:
                scores[d - 1] *= 2
            score *= 2

        scores.append(score)

    # 최종 점수 구하기
    answer = sum(scores)

    return answer