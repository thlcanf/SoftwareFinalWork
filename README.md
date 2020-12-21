# 软件与技术操作演示程序 
简介：该程序主要能够实现`二叉树的基本操作的演示`，如`插入删除元素`、`前后中序遍历`等，以及实现两类排序方式：`冒泡法`和`快速排序法`的动画演示。
源码地址：https://github.com/thlcanf/SoftwareFinalWork
## 实现效果
![image](https://github.com/thlcanf/SoftwareFinalWork/blob/main/bucto.gif)
## 操作方法：
文件已经打包成exe文件，直接运行`Mysoft.exe`便可以查看效果。
## 文件说明
    Mysoft.py------运行主程序
    bubbleSort.py、quickSort.py------冒泡法和快速法
    mainshow.py------将上述两类算法包装成GUI
    BinarySearch.py------BST二叉树主要源码
    Circular_queue.py------循环队列显示程序
### python库函数
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
