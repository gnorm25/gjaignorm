def solution(my_string): 
    ttt= list(my_string)
    ooo= list(set(my_string))
    xxx= []
    for x in ttt: 
        if x in ooo: 
            ooo.remove(x)
            xxx.append(x)
    return ''.join(xxx)
            
        