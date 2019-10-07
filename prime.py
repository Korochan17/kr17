from math import sqrt
import time
from sys import argv

n = int(argv[1])

start = time.process_time()

x = 2
primeList = []
while len(primeList) < n:
    sqrtx = sqrt(x)
    for j in primeList:
        if j > sqrtx:
           primeList.append(x)
           break
        if x % j == 0:
            break
    else:
        primeList.append(x)
    x += 1

end = time.process_time()
during = end - start
print(primeList[-1], during)
