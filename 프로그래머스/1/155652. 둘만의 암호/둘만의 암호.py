def solution(s, skip, index):
    answer = ''
    keys= 'abcdefghijklmnopqrstuvwxyz'*100
    for x in s: 
        ori_dx= keys.index(x)
        for y in range(index): 
            ori_dx+= 1
            while keys[ori_dx] in skip: 
                ori_dx+= 1 
        answer+= keys[ori_dx]

    
    return answer