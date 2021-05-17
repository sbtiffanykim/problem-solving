# 계수 정렬
# time complexity: O(n+k) k: 데이터의 최댓값 (최악의 경우에도 보장됨)
# 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수는 없다

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언한 후 모든 값을 0으로 초기화
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=" ")
