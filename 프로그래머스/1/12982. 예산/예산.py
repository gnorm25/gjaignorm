def solution(d, budget):
    d.sort()
    for xi, xvalue in enumerate(d): 
        
        budget-=xvalue
        if budget<0: 
            return xi
    
    return len(d)