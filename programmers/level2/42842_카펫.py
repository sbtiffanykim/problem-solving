def solution(brown, yellow):
    # 3 * 3 이상이어야 함
    answer = []

    # 총 타일의 갯수
    total = brown + yellow

    # 총 타일을 n * m 형태로 나타내기 위해 3부터 차례대로 나누어 봄
    # 충분히 큰 숫자를 넣기 위해 rough하게 갈색 타일의 반(8~5000)까지 limit으로 설정
    for i in range(3, 2500):
        a = total / i
        # 전체 타일에서 양 끝을 뺀 네모와 노란 타일의 개수가 같을 때
        if (i - 2) * (a - 2) == yellow:
            # 가로의 길이가 더 길기 때문에 가로를 큰 수로 지정
            answer.append(a)
            answer.append(i)
            break

    return answer