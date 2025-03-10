# task1
def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)


# task2
import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(middle))

# Приклад використання
arr = [3, 1, 5, 9, 2, 8, 7, 4, 6]
print("Min & Max:", find_min_max(arr))
print("3-й найменший елемент:", quick_select(arr, 3))