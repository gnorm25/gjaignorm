def solution(N, stages): 
    answer = [] 
    retired= {} 
    surv_num= len(stages) 
    for x in range(1, N+1): 
        if surv_num<=0: 
            break 
        retired.setdefault(x, stages.count(x)/surv_num) 
        surv_num-=stages.count(x) 
    so = sorted(retired.items(), key= lambda item:item[1], reverse= True) 
    for x in so: 
        answer.append(x[0]) 
    while len(answer)<N: 
        answer.append(len(answer)+1) 
    return answer 