def solution(n):
    nuu=[]
    for x in range(n): 
        if n%(x+1)==0: 
            nuu.append(x+1)
    return nuu