with open('input.txt') as input:
    position = 0
    chars = []
    while char := input.read(1):
        position += 1
        chars.append(char)
        chars = chars[-4:]
        if len(chars) == 4 and not any((chars.count(item)>1) for item in chars):
            break

    print(f"start-of-packet marker position: {position}")