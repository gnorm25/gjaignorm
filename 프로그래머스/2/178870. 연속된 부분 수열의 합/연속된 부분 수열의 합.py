def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    best_start, best_end = 0, float('inf')
    
    while end < len(sequence):
        current_sum += sequence[end]
        
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
            
        if current_sum == k:
            if end - start < best_end - best_start:
                best_start, best_end = start, end
        
        end += 1
    
    return [best_start, best_end]






# def solution(sequence, k):
#     pluu=[]
#     getcha=[]
#     lnn=[]
#     lee=100000
#     i=0
    
#     susu=0
#     a=0
#     l=0
#     fi=0
    
#     while l<len(sequence)+1: 
#         susu=sum(sequence[a:l])
#         if susu<k:
#             l+=1
#         elif susu>k: 
#             a+=1
#         else: 
#             if l-a<lee: 
#                 getcha=[a,l-1]
#                 lee= l-a
#             l+=1

            
    
#     for x in sequence: 
        
#         pluu.append(x)
        
#         while sum(pluu)>k:
#             pluu.pop(0)
            
#         if sum(pluu)==k: 
#             lnn=[i-len(pluu)+1, i]
#             if lee>lnn[-1]-lnn[0]: 
#                 lee=lnn[-1]-lnn[0]
#                 getcha=lnn
#         i=i+1
