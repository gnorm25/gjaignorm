def solution(n):
    answer= [] 
    for x in range(n+1): 
        if x%2!=0: 
            answer.append(x)
            
    return answer