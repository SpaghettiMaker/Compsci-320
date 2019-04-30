import random

# creates text file 'text1.txt'
# which you can use to check the correctness and runtime for select.py

# load the file into your select.py program
# via the terminal 'python3 select.py < test1.txt'
# or type it out if you're keen


# max sets the maximum length for the list
# note that 10^7 or 8 does take a while
max = 10**6
f1 = open('test1.txt','w')
f1.write(str(max-1) + ' ' + str(random.randrange(1,max)) + '\n')

for i in range(1,max-1):
    if i == max/10: print("10%")
    if i == max/10*2: print("20%")
    if i == max/10*3: print("30%")
    if i == max/10*4: print("40%")
    if i == max/10*5: print("50%")
    if i == max/10*6: print("60%")
    if i == max/10*7: print("70%")
    if i == max/10*8: print("80%")
    if i == max/10*9: print("90%")
    if i == max-2: print("100%")
    r = str(random.randrange(1,2**32))
    f1.write(r+'\n')
f1.write(str(random.randrange(1,2**32))+'\n')    
f1.write("0 0")
f1.close()
print("Done!")
