# 집합 자료형(set) 이용

n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
store = set(map(int, input().split()))
m = int(input())
needs = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for n in needs:
    # 해당 부품이 존재하는 지 확인
    if n in store:
        print("yes", end=" ")
    else:
        print("no", end=" ")
