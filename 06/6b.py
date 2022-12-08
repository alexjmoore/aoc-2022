with open('input.txt') as input:
    position = 0
    chars = []
    while char := input.read(1):
        position += 1
        chars.append(char)
        chars = chars[-14:]
        if len(chars) == 14 and not any((chars.count(item)>1) for item in chars):
            break

    print(f"start-of-message marker position: {position}")