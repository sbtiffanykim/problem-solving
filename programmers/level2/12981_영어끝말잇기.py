def solution(n, words):

    last_chr = words[0][-1]
    prev_words = [
        words[0],
    ]
    person, turn = 0, 0
    for i in range(1, len(words)):
        # 첫글자가 전의 글자의 마지막 글자와 다르면 탈락
        if words[i][0] != last_chr:
            # 탈락자 구하기
            person = i % n + 1
            # 탈락한 사람의 차례 구하기
            turn = i // n + 1
            break
        # 이미 말한 적이 있으면 탈락
        elif words[i] in prev_words:
            person = i % n + 1
            turn = i // n + 1
            break
        # 통과하는 경우에는 말한 단어를 저장하고, 마지막 글자를 업데이트 하기
        else:
            prev_words.append(words[i])
            last_chr = words[i][-1]

    return [person, turn]