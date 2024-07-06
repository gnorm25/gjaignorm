def solution(food):
    answer= []
    for cal in range(1, len(food)): 
        for x in range((food[cal])//2): 
            answer.append(str(cal))
    answer= ''.join(answer)
    return answer+'0'+answer[::-1]
