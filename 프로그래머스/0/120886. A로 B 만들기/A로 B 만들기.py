def solution(before, after):
    count=0
    flfl=list(before)
    for x in after: 
        if x in flfl: 
            count+=1
            flfl.remove(x)
            
    if count==len(before): 
        return 1
    else:
        return 0