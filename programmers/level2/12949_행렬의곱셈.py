def solution(arr1, arr2):
    answer = []
    # arr2의 col별로 묶어 새로운 리스트 만들기
    col_2 = list(zip(*arr2))

    for i in range(len(arr1)):
        temp = []
        # arr1의 row별로 계산
        row_1 = arr1[i]
        for j in range(len(col_2)):
            # arr1의 row와 arr2의 col을 곱하고 더해 matrix 곱셈 수행
            a = sum(map(lambda x, y: x * y, row_1, col_2[j]))
            temp.append(a)
        answer.append(temp)

    return answer


"""
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
# [[15, 15], [15, 15], [15, 15]]

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
"""