def solution(numbers, hand):
    answer = ""
    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2),
    }

    cur_left = "*"
    cur_right = "#"

    def distance(hand, number):
        return abs(hand[0] - number[0]) + abs(hand[1] - number[1])

    for n in numbers:

        if n in [1, 4, 7]:
            answer += "L"
            cur_left = n
        elif n in [3, 6, 9]:
            answer += "R"
            cur_right = n
        elif n in [2, 5, 8, 0]:
            left_dis = distance(keypad[cur_left], keypad[n])
            right_dis = distance(keypad[cur_right], keypad[n])

            if left_dis < right_dis:
                answer += "L"
                cur_left = n
            elif left_dis > right_dis:
                answer += "R"
                cur_right = n

            elif left_dis == right_dis:
                if hand == "right":
                    answer += "R"
                    cur_right = n
                else:
                    answer += "L"
                    cur_left = n
    return answer