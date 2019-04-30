import sys

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

sys.setrecursionlimit(100000)
data_set_number = 1
global_index = 0
global_array = sys.stdin.read().split("\n")

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
