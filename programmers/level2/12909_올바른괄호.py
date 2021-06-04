def solution(s):
    answer = True

    stack = []
    if s[0] == ")" or s[-1] == "(":
        return False
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")" and len(stack) > 0:
            stack.pop()

    if stack:
        answer = False

    return answer


"""
print(solution("()()"))  # true
print(solution("(())()"))  # true
print(solution(")()("))  # false
print(solution("(()("))  # false
"""