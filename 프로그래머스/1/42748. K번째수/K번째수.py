def solution(array, commands):
    answer=[]
    for x, y, z in commands: 
        tt= array[x-1:y]
        tt.sort()
        answer.append(tt[z-1])
    return answer