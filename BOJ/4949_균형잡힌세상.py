import sys

input = sys.stdin.readline

while True:
    flag = True
    opened_brackets = []
    string = input().rstrip()

    # 점 하나만 입력으로 들어오면 종료
    if string == ".":
        break

    for c in string:
        # 열린 괄호들은 stack에 넣기
        if c == "(":
            opened_brackets.append(c)
        elif c == "[":
            opened_brackets.append(c)
        # 닫힌 괄호는 짝이 맞고, stack이 맞는 지 확인한 후 맞으면 stack pop 실행
        elif c == ")":
            if not opened_brackets or opened_brackets[-1] != "(":
                flag = False
            else:
                opened_brackets.pop()
        elif c == "]":
            if not opened_brackets or opened_brackets[-1] != "[":
                flag = False
            else:
                opened_brackets.pop()

    # 다 끝난 후에도 stack에 괄호가 남아있다면 균형이 잡히지 않았다
    if opened_brackets:
        flag = False

    if flag:
        print("yes")
    else:
        print("no")