import random as r
randnum = r.randrange(1,30)
print("Number to be gussed...",randnum)
i =1

while True:
    print("number guessed :", i)
    if(i == randnum):
        print("Rando number has been guessed correctly Congrates")
        #break and exits from the loop
        break
    i +=1
print("the program is completed.")
