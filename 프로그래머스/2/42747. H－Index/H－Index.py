def solution(citations):
    citations.sort(reverse= True)
    for x in range(len(citations), 0, -1): 
        if citations[x-1]>=x:
            return x
    else: 
        return 0