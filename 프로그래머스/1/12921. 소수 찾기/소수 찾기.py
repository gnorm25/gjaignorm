def solution(n):
    num_list= set(range(3, n+1, 2))
    new_list=num_list.copy()
    
    
    for num in num_list: 
        new_list-=set(range(num*2,n+1,num))
        

    return len(new_list)+1