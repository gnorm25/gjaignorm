def solution(friends, gifts): 
    index= {friend: [0] for friend in friends}
    answer= {friend: 0 for friend in friends}
    for x in gifts: 
        give, receive = x.split()
        index[give][0]+= 1 
        index[receive][0]-= 1 
        index[give].append(receive)
    for x in range(len(friends)-1): 
        for y in range(x+1, len(friends)): 
            a= index[friends[x]].count(friends[y])
            b= index[friends[y]].count(friends[x])
            if a==b: 
                if index[friends[x]][0]>index[friends[y]][0]:
                    answer[friends[x]]+= 1
                elif index[friends[x]][0]<index[friends[y]][0]:
                    answer[friends[y]]+= 1
            elif a>b: 
                answer[friends[x]]+= 1
            else: 
                answer[friends[y]]+= 1
    return max(answer.values())
        