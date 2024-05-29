def solution(num_list, n):
    suu=[]
    nuu=[]
    i=0
    for x in num_list: 
        i+=1
        nuu.append(x)
        if i%n==0: 
            suu.append(nuu)
            nuu=[]
    answer = suu
    return answer