def solution(my_string):
    table=str.maketrans({'a':'', 'e':'', 'i':'', 'o':'', 'u':''})
    return my_string.translate(table)

