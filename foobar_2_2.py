def solution(x, y) :
    position = int(0)
    position = int((x(x+1))/2)
    for i in range(y-1) :
        position = position+x+i
    return position
