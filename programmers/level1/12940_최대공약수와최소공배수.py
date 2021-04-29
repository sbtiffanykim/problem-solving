"""
#12940: 최대공약수와 최소공배수
"""

from math import gcd


def solution(n, m):
    answer = []

    # gcd
    answer.append(gcd(n, m))
    # lcm
    answer.append(n * m / gcd(n, m))

    return answer