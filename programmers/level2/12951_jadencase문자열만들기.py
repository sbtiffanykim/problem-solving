def solution(s):
    answer = ""

    # 공백을 기준으로 단어별로 끊어서 리스트에 저장
    words = list(s.split(" "))

    for w in words:
        # 모두 소문자화
        w = w.lower()
        # 첫번째 문자만 대문자 처리
        w = w.capitalize()
        # 단어로 구분 짓기 위해 띄어쓰기 추가하여 문장으로 다시 변환
        answer += w + " "

    # 마지막 공백 없애기
    # 원래 문장에 공백이 두개 있을 경우 마지막 공백만을 없애기 위해 rstrip 쓰지 않음
    if answer[-1] == " ":
        answer = answer[:-1]

    return answer