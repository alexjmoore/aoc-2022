count = 0
for line in open('input.txt'):
    elf1, elf2 = line.strip().split(',')
    elf1_lower, elf1_upper = map(int, (elf1.split('-')))
    elf2_lower, elf2_upper = map(int, (elf2.split('-')))
    if (elf1_lower >= elf2_lower and elf1_upper <= elf2_upper) or \
        (elf2_lower >= elf1_lower and elf2_upper <= elf1_upper):
        count+=1

print(f"fully overlapped assignment pairs: {count}")