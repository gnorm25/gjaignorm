def solution(s):
    flfl=list(s)
    answer = ''.join(sorted(flfl, reverse=True))
    return answer