def solution(record):
    temp = []
    answer = []
    names = dict()

    for r in record:
        r = list(r.split(" "))
        if r[0] == "Enter":
            temp.append(f"{r[1]} 들어왔습니다.")
            names.update({r[1]: r[2]})
        elif r[0] == "Leave":
            temp.append(f"{r[1]} 나갔습니다.")
        else:
            names.update({r[1]: r[2]})

    for t in temp:
        t = t.split(" ")
        t[0] = names[t[0]] + "님이 "
        t = "".join(t)
        answer.append(t)

    return answer