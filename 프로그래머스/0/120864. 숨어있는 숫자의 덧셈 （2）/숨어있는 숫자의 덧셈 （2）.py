# def solution(my_string):
#     table=str.maketrans('abcdefghijklmnopqrstuvwxyz', '                          ')
#     my_string= my_string.lower()
#     ekqekq= my_string.translate(table).split(' ')
#     ekqekq1= ' '.join(ekqekq).split()
#     return sum(list(map(int, ekqekq1)))


# def solution(my_string):
#     answer= []
#     for i in my_string: 
#         if i.isdigit(): 
#             answer.append(i)
#         else: 
#             answer.append(" ")


def solution(my_string): 
    answer= 0
    temp= ''
    for i in my_string: 
        if i.isdigit(): 
            temp += i
        else: 
            if temp: 
                answer += int(temp)
                temp= ''
    if temp: 
        answer += int(temp)
    return answer
