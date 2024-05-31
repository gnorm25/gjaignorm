def solution(arr1, arr2):
    wjdekq2=[]
    for x, y in zip(arr1, arr2): 
        wjdekq=[]
        for a, b in zip(x, y):
            wjdekq.append(a+b)
        wjdekq2.append(wjdekq)
    
    return wjdekq2