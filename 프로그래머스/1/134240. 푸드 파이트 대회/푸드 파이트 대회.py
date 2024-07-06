def solution(food):
    answer= []
    for cal in range(1, len(food)): 
        for x in range((food[cal])//2): 
            answer.append(str(cal))
    answer.append('0')
    answer2= answer[::-1]
    del answer2[0]
    return ''.join(answer+answer2)
