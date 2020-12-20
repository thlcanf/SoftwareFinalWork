import time

def partition(data, head, tail, drawData, speed, size):
    border = head       #set border value at start of partition and pivot at the end
    pivot = data[tail]

    drawData(data, size, getColorArray(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head,tail):  #iterate between border and pivot
        if data[j] < pivot: #if item is smaller than pivot, swap it with the border and increment
            drawData(data, size, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(speed)

            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, size, getColorArray(len(data), head, tail, border, j))
        time.sleep(speed)

    #after iteration, swap border and tail values
    drawData(data, size, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(speed)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, speed, size):
    #exit statement
    if head < tail:
        #initial partition
        partIndex = partition(data, head, tail, drawData, speed, size)
    
        #----Recursive Calls----
        #LEFT PARTITION [uses partIndex-1 because partIndex is in correct spot already]
        quick_sort(data, head, partIndex-1, drawData, speed, size)
        
        #RIGHT PARTITION [same logic as left partition except right side]
        quick_sort(data, partIndex+1, tail, drawData, speed, size)

def getColorArray(dataLen, head, tail, border, currIdx, isSwapping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('royal blue')
        else:
            colorArray.append('blue2')
        
        if i == tail:
            colorArray[i] = 'red'
        elif i == border:
            colorArray[i] = 'red3'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'
    return colorArray