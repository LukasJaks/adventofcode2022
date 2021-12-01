lines = []

with open(r"C:\\Users\\lukas\Desktop\\adventofcode2022\\python\day1_1.txt") as f:
        for line in f:
            lines.append(int(line.split("\n")[0]))

last = 0
total = -1

for x in range(len(lines)-2):
    sum = lines[x] + lines[x+1] + lines[x+2]
    if(sum > last):
        total += 1
    last = sum

print(total)

