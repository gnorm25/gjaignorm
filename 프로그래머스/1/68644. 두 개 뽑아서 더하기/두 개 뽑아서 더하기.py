from itertools import combinations
def solution(numbers):
    wjd= list(combinations(numbers, 2))
    thd= []
    for x, y in wjd: 
        thd.append(x+y)
    thd=list(set(thd))
    thd.sort()
    return thd