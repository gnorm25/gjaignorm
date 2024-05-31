def solution(s):
    rotnp=0
    rotny=0
    rotnp+=s.count('p')
    rotnp+=s.count('P')
    rotny+=s.count('y')
    rotny+=s.count('Y')
    
    if rotnp==rotny: 
        return True
    else: 
        return False
    
