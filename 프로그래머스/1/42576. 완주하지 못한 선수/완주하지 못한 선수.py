# def solution(participant, completion):
#     for x in completion: 
#         participant.remove(x)
#     return ''.join(participant)

def solution(participant, completion):
    my_dict={}
    for x in participant: 
        if x in my_dict: 
            my_dict[x]+= 1
        else: 
            my_dict[x]= 1
    for y in completion: 
        my_dict[y]-= 1
    return ''.join([k for k, v in my_dict.items() if v == 1])