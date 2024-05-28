def solution(cipher, code):
    xxx=list(cipher)
    cc=0
    toto=[]
    for i in xxx: 
        cc+=1
        if cc%code==0: 
            toto.append(i)
    answer = ''.join(toto)
    return answer