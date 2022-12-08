elves = [0]
count = 0
for line in open('input.txt'):
    if line.isspace():
        count+=1
        elves.append(0)
        continue
    elves[count]+=int(line)

elves.sort(reverse=True)
print(f"most calories: {elves[0]}")
print(f"top 3: {elves[0]+elves[1]+elves[2]}")
