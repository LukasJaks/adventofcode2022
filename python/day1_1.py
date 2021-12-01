last = 0
total = -1

with open(r"C:\\Users\\lukas\Desktop\\adventofcode2022\\python\day1_1.txt") as f:
    for line in f:
        l = int(line.split("\n")[0])
        if(l > last):
            total += 1
        last = l

print(total)