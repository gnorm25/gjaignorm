def solution(numbers, direction): 
    
    nuu=list(range(0, len(numbers)))
    
    if direction=='right': 
        for y in range(len(numbers)): 
            nuu[y]=numbers[y-1]
    
    if direction=='left': 
        for x in range(len(numbers)):  
            nuu[x-1]=numbers[x]
    answer = nuu
    return answer