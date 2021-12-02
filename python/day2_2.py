lines = []
horPos = 0
verPos = 0
aim = 0

with open(r"C:\\Users\\lukas\Desktop\\adventofcode2022\\python\day2_1.txt") as f:
        for line in f:
            temp = (line.split("\n")[0]).split(" ")
            lines.append([temp[0], int(temp[1])])

        for line in lines:
            if(line[0]=="forward"):
                horPos += line[1]
                verPos += aim * line[1]
            elif(line[0]=="down"):
                aim += line[1]
            else:
                aim -= line[1]
            print("s")

print(horPos*verPos)