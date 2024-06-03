def solution(nums):
    dkswnd = list(dict.fromkeys(nums))
    
    if len(dkswnd)>=len(nums)//2: 
        return len(nums)//2
    else: 
        return len(dkswnd)
    
# def solution(nums): 
    