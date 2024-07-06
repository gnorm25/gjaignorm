def solution(food):
    answer= ''
    for cal in range(1, len(food)): 
        for x in range((food[cal])//2): 
            answer+= str(cal)
    return answer+'0'+answer[::-1]
