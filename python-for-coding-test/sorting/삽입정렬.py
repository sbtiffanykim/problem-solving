# 삽입 정렬
# 특정한 데이터를 적절한 위치에 삽입하기
# time complexity: O(n^2)
# 특징: 거의 다 정렬되어있는 상태의 데이터라면 매우 빠르게(O(N))으로 동작

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫번째 데이터는 정렬이 되어있다고 생각하고 두번째(index #1)부터 시작
for i in range(1, len(array)):
    # index i부터 1까직 1씩 감소하면서
    for j in range(i, 0, -1):
        # 한칸씩 이동하면서 자기 자신보다 큰 숫자를 만나면
        if array[j] < array[j - 1]:
            # swap
            array[j], array[j - 1] = array[j - 1], array[j]
        # 자기 자신보다 큰 숫자를 만나면 그 위치에서 멈춤
        else:
            break
