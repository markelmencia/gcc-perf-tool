import random
import sys

n = int(sys.argv[1])

with open("data.txt", "w") as file:
    file.write(f"{n},")
    
    for i in range(n):
        num = random.randint(0, n)  # rango configurable
        if i < n - 1:
            file.write(f"{num},")
        else:
            file.write(f"{num}")

    file.write(f";")
