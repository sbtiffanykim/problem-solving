def solution(skill, skill_trees):
    answer = 0
    # skill에 들어있는 스킬을 각각 리스트에 넣기
    alpha = list(skill)
    for t in skill_trees:
        # 유저 스킬트리 중에 alpha에 있는 것만 temp에 넣기
        temp = list(filter(lambda x: x in alpha, t))

        # 만약 선행 스킬트리와 가공한 유저 스킬트리의 길이가 같을 때
        if len(skill) == len(temp):
            # 둘이 동일하다면 가능한 스킬트리임
            if skill == "".join(temp):
                answer += 1
        else:
            # 가공한 유저 스킬트리의 길이를 구함
            n = len(temp)
            # 선행, 후행을 모두 고려하였을 때
            # 선행 스킬트리에서 가공한 유저 스킬트리의 길이만큼 잘랐을 때 둘이 동일하다면 가능한 스킬트리임
            # eg) 선행: "CBAD" => "CB" // 유저: "CB"
            if skill[:n] == "".join(temp):
                answer += 1

    return answer


"""
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))   # 2
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "ACD"]))   # 2
"""