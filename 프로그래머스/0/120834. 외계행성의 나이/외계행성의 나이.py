def solution(age):
    dkfvk=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cnffur=[]
    for x in str(age): 
        cnffur.append(dkfvk[int(x)])
    answer=''.join(cnffur)
        
    return answer