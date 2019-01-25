import math


for i in range(541, 0, -2):
    isPrime = True
    for x in range(1, round(math.sqrt(i))):
        print(i/x)
        if type(i/x) is int: #Skilar alltaf false.
            isPrime = False
    #if isPrime:
        #print(i)
print(2)