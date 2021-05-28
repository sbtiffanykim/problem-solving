def solution(s):
    answer = ""

    nums = list(map(int, s.split()))

    max_num = max(nums)
    min_num = min(nums)

    answer = str(min_num) + " " + str(max_num)

    return answer