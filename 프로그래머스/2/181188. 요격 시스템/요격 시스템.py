def solution(targets):
    answer = 0
    targets.sort()
    
    while targets: 
        point= targets[-1][0]
        while targets and point<targets[-1][1]: 
            targets.pop(-1)
        answer+= 1
    return answer
        
    
