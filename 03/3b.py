import string
ELF_GROUP_SIZE = 3

priorities = 0
alphabet = list(string.ascii_letters)

with open('input.txt') as input:
    lines = []
    for line in input:
        lines.append(line)
        if len(lines) >= ELF_GROUP_SIZE:
            for char in lines[0].strip():
                if char in lines[1] and char in lines[2]:
                    priorities += alphabet.index(char) + 1
                    break
            lines = []

print(f"sum of priorities of group badge: {priorities}")