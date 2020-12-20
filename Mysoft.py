#-*- coding:utf-8 -*-  
##主窗口设定
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from mainshow import mainsh
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import Circular_queue as CQ 
import tkinter.ttk
from BinarySearch import mainbst
import ctypes
#操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#获取屏幕的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root = Tk()
root.geometry('1300x750')
root.title('软件技术基础操作演示')
root.iconbitmap("buct.ico")
#设置程序缩放以适应屏幕达到较佳显示效果
root.call('tk', 'scaling', ScaleFactor/75)
notebook = ttk.Notebook(root)
framestart = Frame()
frameOne = Frame()
frameTwo = Frame()
##framestart
canvass = Canvas(framestart, bg='white', height=750, width=1300)
#加载图片
image_files = PhotoImage(file='bucto.gif')
#定义图片的位置
images = canvass.create_image(10, 10, anchor='nw', image=image_files)
canvass.pack()

##frameOne
button = Button(frameOne, text='点击进入二叉树演示',fg='red',bg='white',padx=1, pady=1, command=mainbst)
button.pack()
# 添加图片
canvas1 = Canvas(frameOne, bg='white', height=750, width=1300)
#加载图片
image_file11 = PhotoImage(file='bst.gif')
#定义图片的位置
image2 = canvas1.create_image(180, 10, anchor='nw', image=image_file11)
canvas1.pack()

##frameTwo
button = Button(frameTwo, text='点击进入演示',fg='red',bg='white',padx=1, pady=1, command=mainsh)
button.pack()
#图片显示
canvas = Canvas(frameTwo, bg='white', height=750, width=1300)

#加载图片1
image_file = PhotoImage(file='quick.gif')
#加载图片2
image_file1 = PhotoImage(file='bubble.gif')

#定义图片1的位置
image1 = canvas.create_image(40, 40, anchor='nw', image=image_file1 )
#定义图片2的位置
image = canvas.create_image(700, 40, anchor='nw', image=image_file)
canvas.pack()
notebook.add(framestart,text='程序介绍')
notebook.add(frameOne, text='二叉树演示')
notebook.add(frameTwo, text='排序算法演示')
notebook.pack(padx=10, pady=5, fill=BOTH, expand=True)
root.mainloop()
