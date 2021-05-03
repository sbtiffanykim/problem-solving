n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 가장 큰 수와 두번째로 큰 수만 반복해서 더하면 가장 큰 수를 만들어 낼 수 있다

nums.sort(reverse=True)  # 입력받은 수들을 내림차순으로 정렬
first = nums[0]  # 가장 큰 수
second = nums[1]  # 두번째로 큰 수

# 가장 큰 수는 (m // k) 세트씩 k번 더하기
# 가장 작은 수는 m을 k로 나눈 나머지의 개수만큼 더하기
answer = first * (m // k) * k + second * (m % k)
print(answer)