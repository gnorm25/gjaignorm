def solution(my_string):
    table=str.maketrans('abcdefghijklmnopqrstuvwxyz', '                          ')
    my_string= my_string.lower()
    ekqekq= my_string.translate(table).split(' ')
    ekqekq1= ' '.join(ekqekq).split()
    return sum(list(map(int, ekqekq1)))