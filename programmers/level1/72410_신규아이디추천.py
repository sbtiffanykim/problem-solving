"""
#72410: 신규 아이디 추천
"""

import re


def solution(new_id):
    answer = ""

    # stage 1
    new_id = new_id.lower()

    # stage 2
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)

    # stage 3
    new_id = re.sub("\.+", ".", new_id)

    # stage 4
    new_id = re.sub("^[.]|[.]$", "", new_id)

    # stage 5
    if len(new_id) == 0:
        new_id += "a"

    # stage 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub("[.]$", "", new_id)

    # stage 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id

    return answer