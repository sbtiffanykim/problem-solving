import math

num = input()
cards = [0] * 10

for n in num:
    cards[int(n)] += 1

# 6,9는 서로 뒤집어서 사용할 수 있으므로 이 때를 고려하여 필요한 카드의 개수 구하기
six_nine_cards = math.ceil((cards[6] + cards[9]) / 2)
# 6, 9를 표현하는 데 필요한 카드의 수는 위에서 구했으므로 0으로 설정
cards[6] = 0
cards[9] = 0
# 6, 9를 제외한 카드 중에 가장 많은 수를 필요로 하는 카드 번호를 고른다
max_cards = max(cards)

# 6/9를 표현하는 카드수가 더 많이 필요할 경우
if max_cards < six_nine_cards:
    print(six_nine_cards)
# 둘을 제외한 카드 중에 가장 많은 수를 필요로 하는 카드가 있을 경우
else:
    print(max_cards)
