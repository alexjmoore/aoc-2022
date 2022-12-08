import string
priorities = 0
alphabet = list(string.ascii_letters)

for line in open('input.txt'):
    comp1, comp2 = line[:int(len(line)/2)], line[int(len(line)/2):]
    for char in comp1:
        if char in comp2:
            priorities += alphabet.index(char) + 1
            break

print( f"sum of priorities: {priorities}")