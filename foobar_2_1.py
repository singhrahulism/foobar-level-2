def solution(src,dest) :
    lstSteps = []
    lstStepsTemp = []
    iterationCount = int(0)
    steps = int(1)
    stopNow = int(0)
    lstSteps = possibleMoves(src)
    if src == dest :
        return 0
    for search in lstSteps :
        if search == dest :
            break
    else :
        while True :
            steps = steps+1
            for i in lstSteps :
                lstStepsTemp.append(i)
            iterationCount = len(lstStepsTemp)
            del lstSteps[:]
            for i in range(iterationCount) :
                lstSteps = lstSteps+possibleMoves(lstStepsTemp[i])
            for search in lstSteps :
                if search == dest :
                    stopNow = 1
                    break
            if stopNow == 1 :
                break
    del lstStepsTemp[:]
    del lstSteps[:]
    return steps
def possibleMoves(pos) :
    y = int(int(pos/8)+1)
    x = int(pos-(8*(y-1))+1)
    lstCoor = [[x-1, y-2], [x+1, y-2], [x-2, y-1], [x+2, y-1], [x-2, y+1], [x+2, y+1], [x-1, y+2], [x+1, y+2]]
    lstPos = []
    totalMoves = int(0)
    for i in range(0, 8) :
        for j in range(0, 2) :
            if lstCoor[totalMoves][j] < 1 or lstCoor[totalMoves][j] > 8 :
                lstCoor.pop(totalMoves)
                break
        else :
            totalMoves = totalMoves+1
    for i in range(0, totalMoves) :
        lstPos.append(lstCoor[i][0]+(8*(lstCoor[i][1]-1))-1)
    return lstPos

print(solution(0, 0))
