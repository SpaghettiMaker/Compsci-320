import sys


def peg(lst, size):
    global peg_count
    left_temp = list(lst)
    left_size = int(size)
    right_temp = list(lst)
    right_size = int(size)
    for num in range(11, -1, -1):
        if lst[num] == 'o':
            if num - 2 >= 0 and lst[num - 1] == 'o' and lst[num - 2] == '-':  # try left jump
                left_temp[num] = '-'
                left_temp[num - 1] = '-'
                left_temp[num - 2] = 'o'

                left_size -= 1
                if left_size < peg_count:
                    peg_count = left_size
                peg(left_temp, left_size)

            if num + 2 <= 11 and lst[num + 1] == 'o' and lst[num + 2] == '-':  # try right jump
                right_temp[num] = '-'
                right_temp[num + 1] = '-'
                right_temp[num + 2] = 'o'

                right_size -= 1
                if right_size < peg_count:
                    peg_count = right_size
                peg(right_temp, right_size)

file = open("input.txt", "r")
lines = file.read().split("\n")
#lines = sys.stdin.read().split("\n")
i = int(lines[0])
k = 1

while i >= k:
    count = 0
    for pegs in lines[k]:
        if pegs == 'o':
            count += 1

    peg_count = count
    peg(list(lines[k]), count)
    print(peg_count)
    k += 1




