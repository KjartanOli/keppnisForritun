import math

for i in range(541, 0, -2):
    isPrime = True
    for x in range(2, round(math.sqrt(i))):
        if i % x == 0:
            isPrime = False
    if isPrime:
        print(i)
print(2)