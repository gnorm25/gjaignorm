def solution(n):
    
    x=[i for i in range(1, int(n/2+1)) if n%i==0]
    return len(x)+1
    
# def solution(n): 
#     return len(list(filter(lambda x: n%(x+1)==0, range(0))))

# def solution(n): 
#     x=[i for i in range(n//2, 0, -1) if n%i==0]
#     return len(x)+1
        