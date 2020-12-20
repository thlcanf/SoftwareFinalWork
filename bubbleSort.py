#bubble sort algorithm implementation for interactiveSorting
import time

def bubble_sort(data, drawData, speed, size):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, size, ['green' if x == j or x == j+1 else 'blue' for x in range(len(data))]) 
                time.sleep(speed)