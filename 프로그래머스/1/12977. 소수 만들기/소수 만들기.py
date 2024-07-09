import itertools
def solution(nums):
    a= list(itertools.combinations(nums, 3))
    cnt2= 0
    for i in a: 
        b= sum(i)
        cnt= 0
        for j in range(2, b): 
            if b%j==0: 
                cnt+= 1
            if cnt>=1: 
                break
        if cnt<1: 
            cnt2+= 1 
    return cnt2
            
            
    
    