import sys
import time

def select(lst, left, right, index):
    if left == right:
        return lst[left]

    x = lst[left] - lst[right//2]
    y = lst[right//2] - lst[right]
    z = lst[left] - lst[right]
    if x * y > 0:
        pivot_index = right//2
    elif x * z > 0:
        pivot_index = right - 1
    else:
        pivot_index = left

    lst[left], lst[pivot_index] = lst[pivot_index], lst[left]
    temp = left

    for item in range(left + 1, right + 1):
        if lst[item] < lst[left]:
            temp += 1
            lst[temp], lst[item] = lst[item], lst[temp]

    lst[temp], lst[left] = lst[left], lst[temp]

    if index == temp:
        return lst[temp]
    elif index < temp:
        return select(lst, left, temp - 1, index)
    else:
        return select(lst, temp + 1, right, index)

def quick_select(items, kth_index):
    left = 0
    right = len(items) - 1
    return select(items, left, right, kth_index)

start = time.time()
sys.setrecursionlimit(100000)
data_set_number = 1
global_index = 0
#global_array = sys.stdin.read().split("\n")
file_obj = open("test1.txt", "r")
global_array = file_obj.read().split("\n")
#global_array = ["2 2", "1", "3", "5 1", "5", "8", "4", "12", "10",
#                "5 3", "7", "1", "6", "8", "9", "0 0"]
while True:
    temp = global_array[global_index].split()
    n = int(temp[0])
    k = int(temp[1])
    if n == 0:
        break

    array = list(map(int, global_array[global_index+1:global_index + n+1]))
    output = quick_select(array, k - 1)
    print("Data set {}: element {} is {}".format(data_set_number, k, output))

    global_index += n + 1
    data_set_number += 1

end = time.time()
print("time is {}ms".format((end - start)*1000))

