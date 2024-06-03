def solution(clothes):
    dhtwkd= {} 
    for name, whd in clothes: 
        if whd in dhtwkd: 
            dhtwkd[whd]+= 1 
        else: 
            dhtwkd[whd]= 1
    answer= 1
    
    for whd in dhtwkd: 
        answer*= dhtwkd[whd]+1
    return answer-1