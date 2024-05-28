def solution(my_string):
    t=0
    fjfj=list(my_string)
    
    for x in fjfj: 
        if type(x)==int: 
            t=t+x
    answer = t
    return answer