def solution(dots):
    horiz=set()
    verti=set()
    for x, y in dots: 
        horiz.add(x)
        verti.add(y)
    hor_len= list(horiz)[0]-list(horiz)[1]
    ver_len= list(verti)[0]-list(verti)[1]
    return abs(hor_len*ver_len)

        