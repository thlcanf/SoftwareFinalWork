from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort

def drawData(data, size, colorArray):
    canvas.delete("all") #redraw canvas everytime generate is pressed
    c_height = 380  #canvas height and width values
    c_width = 600
    x_width = c_width/(len(data)) #Calculated based on # of bars
    offset = 0 #offset and spacing are for appearance
    spacing = 1
    #normalize data to always scale to height
    normData = [i/max(data) for i in data]

    #Creating rectangles
    for i, height in enumerate(normData):
        #top left corner calculation
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 360 #using 360 leaves 20 pixels of space from top of canvas
        #bottom right corner calculation
        x1 = (i+1) * x_width + offset
        y1 = c_height

        #Use create_rectangle with top left, bottom right, and a fill color
        canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
        #Create text just above the bar to indicate the value at i in data
        if(size <= 20):
            canvas.create_text(x0+4, y0, anchor = SW, text = str(data[i]), fill = 'white', font = ("Courier", 8))
    root.update_idletasks()

def generate():
    global root
    global canvas
    global data
    global speedScale
    global sizeEntry
    global minEntry
    global maxEntry
    global algMenu
    minVal = int(minEntry.get())    #min,max,and size are taken from user input in row 1 UI
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    speed = int(speedScale.get())

    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal #swap min/max if min>max

    data = []
    for _ in range(size):   #Create data set of size within min and max range
        data.append(random.randrange(minVal, maxVal+1))
    #call drawData to create rectangles
    drawData(data, size, ['blue' for x in range(len(data))])

def startAlgo():
    global root
    global canvas
    global data
    global algMenu
    global speedScale
    global sizeEntry
    global minEntry
    global maxEntry
    if not data: return
    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get(), sizeEntry.get())
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get(), sizeEntry.get())
    # elif algMenu.get() == 'Merge Sort':
    #     start_mergeSort(data, drawData, speedScale.get(), sizeEntry.get())
    drawData(data, sizeEntry.get(),['navy' for x in range(len(data))])


def mainsh():
    global root
    global canvas
    global data
    global speedScale
    global sizeEntry
    global minEntry
    global maxEntry
    global algMenu

    root = Tk()
    root.title('排序算法演示')
    root.maxsize(900, 600)
    root.config(bg='black')

    #vars
    alg = StringVar()
    data = []   #empty data set, generated randomly
    #frame/base layout

    UI_frame = Frame(root, width = 600, height = 200, bg = 'grey')
    UI_frame.grid(row = 0, column = 0, padx = 3, pady = 5)

    canvas = Canvas(root, width = 600, height = 380, bg = 'black')
    canvas.grid(row = 1, column = 0, padx = 0, pady=0)
#-------UI-----------------------------------
#-------Row[0]-------
    #Algorithm Text and label
    Label(UI_frame, text= "Algorithm:", bg='grey').grid(row = 0, column = 0, padx=0, pady=5, sticky=W)

    #Algorith button, automatically set to Selection Sort
    algMenu = ttk.Combobox(UI_frame, textvariable = alg, values = ['Bubble Sort', 'Quick Sort'])
    algMenu.grid(row = 0, column = 1, padx = 5, pady = 0)
    algMenu.current(0)

    speedScale = Scale(UI_frame, from_=0.1, to=1, length = 200, digits = 2, resolution = 0.1, orient = HORIZONTAL, label = "SPEED[sec]:")
    speedScale.grid(row = 0, column = 2, padx=5,pady=5)

    #Start button
    Button(UI_frame, text="Start", command = startAlgo, bg = 'green', fg = 'white').grid(row = 0, column = 3, padx=5, pady=5)

    #-------Row[1]-------
    #Size scale
    sizeEntry = Scale(UI_frame, from_=5, to=100, length = 200, resolution = 1, orient = HORIZONTAL, label = "n:")
    sizeEntry.grid(row = 1, column = 0, padx = 3, pady = 5)

    #Minimum value label and entry field
    minEntry = Scale(UI_frame, from_=0, to=200, length = 200, resolution = 1, orient = HORIZONTAL, label = "min:")
    minEntry.grid(row = 1, column = 1, padx = 3, pady = 5)

    #Maximum value label and entry field
    maxEntry = Scale(UI_frame, from_=5, to=200, length = 200, resolution = 1, orient = HORIZONTAL, label = "max:")
    maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

    #Generate button
    Button(UI_frame, text="Generate", command = generate, bg = 'blue', fg = 'white').grid(row = 1, column = 3, padx=5, pady=5)
    root.iconbitmap("buct.ico")
    root.mainloop()