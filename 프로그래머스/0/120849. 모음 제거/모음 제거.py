def solution(my_string):
    return list(set(list(my_string))-set(list('aeiou')))