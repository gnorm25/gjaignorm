def solution(n):
    answer=[]
    for x in range(n): 
        nuu=[]
        for y in range(x+1): 
            if (x+1)%(y+1)==0: 
                nuu.append(y+1)
        if len(nuu)>2: 
            answer.append(x+1)
    return len(answer)