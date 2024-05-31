def solution(answers):
    gkr1=[1, 2, 3, 4, 5]*((len(answers)//5)+1)
    gkr2=[2, 1, 2, 3, 2, 4, 2, 5]*((len(answers)//8)+1)
    gkr3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*((len(answers)//10)+1)
    
    gkr1ekq=0
    gkr2ekq=0
    gkr3ekq=0
    
    wjdekq=[]
    
    for x in range(len(answers)): 
        if gkr1[x]==answers[x]: 
            gkr1ekq+=1
        if gkr2[x]==answers[x]: 
            gkr2ekq+=1
        if gkr3[x]==answers[x]: 
            gkr3ekq+=1
            
    
    
            
    if gkr1ekq>gkr2ekq and gkr1ekq>gkr3ekq: 
        return [1]
    elif gkr2ekq>gkr1ekq and gkr2ekq>gkr3ekq: 
        return [2]
    elif gkr3ekq>gkr1ekq and gkr3ekq>gkr2ekq: 
        return [3]
    elif gkr1ekq==gkr2ekq and gkr2ekq==gkr3ekq: 
        return [1, 2, 3]
    elif gkr1ekq==gkr2ekq: 
        return [1, 2]
    elif gkr2ekq==gkr3ekq: 
        return [2, 3]
    elif gkr3ekq==gkr1ekq: 
        return [1, 3]
    
    
    
    
    