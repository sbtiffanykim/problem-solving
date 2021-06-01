def solution(record):
    temp = []
    answer = []
    # 아이디와 이름을 저장하기 위한 dict 선언
    names = dict()

    for r in record:
        # 명령어를 단어별로 구별하기 위해 나누기
        r = list(r.split(" "))
        # 입장할 때
        if r[0] == "Enter":
            temp.append(f"{r[1]} 들어왔습니다.")
            # 아이디와 이름을 dict에 저장
            names.update({r[1]: r[2]})
        # 퇴장할 때
        elif r[0] == "Leave":
            temp.append(f"{r[1]} 나갔습니다.")
        # 닉네임을 바꾸었을 때
        else:
            # 아이디와 바꾼 닉네임을 저장
            names.update({r[1]: r[2]})

    for t in temp:
        t = t.split(" ")
        # 아이디 부분을 별명으로 바꾸기
        t[0] = names[t[0]] + "님이 "
        # 다시 문장으로 변형
        t = "".join(t)
        # 출력하기 위해 추가하기
        answer.append(t)

    return answer