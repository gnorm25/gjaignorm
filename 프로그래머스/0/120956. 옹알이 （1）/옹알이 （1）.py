def solution(babbling):
    tokken= ["aya", "ye", "woo", "ma"]
    answer = 0
    for x in babbling: 
        for y in tokken: 
            x= x.replace(y, ' ')
        x= x.replace(' ', '')
        if len(x)==0: 
            answer+= 1
    return answer