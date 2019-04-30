import sys

def diet_help(triples):
    smallest = 0
    biggest = 1
    big_eaten = 0
    temp = 0
    if triples[0] > triples[1]:
        smallest = 1
        biggest = 0

    time = int(triples[2])
    time_wasted = triples[2] % triples[smallest]
    small_eaten = triples[2] // triples[smallest]

    if time_wasted != triples[2] or time_wasted != 0:
        while time_wasted != 0:
            time -= triples[biggest]
            temp += 1
            if time < 0 or small_eaten == 0:
                break
            if time % triples[smallest] < time_wasted:
                time_wasted = time % triples[smallest]
                small_eaten = time // triples[smallest]
                big_eaten = temp

        return small_eaten + big_eaten, time_wasted

# file_obj = open(sys.argv[1], 'r')
# content = file_obj.readlines()
# content = [x.strip() for x in content]  # removes \n character
while True:
    line = input()
    triple = line.split()
    triple = list(map(int, triple))

    if triple[0] == 0:
        break
    output = diet_help(triple)
    print("{} {}".format(output[0], output[1]))
'''for line in content:
    line.strip()
    triple = line.split()
    triple = list(map(int, triple))

    if triple[0] == 0:
        break
    output = diet_help(triple)
    print("{} {}".format(output[0], output[1]))'''

