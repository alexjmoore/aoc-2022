import string, copy

alphabet = list(string.ascii_lowercase)

x = y = 0
start_x = start_y = 0
end_x = end_y = 0
width = height = 0
heightmap = {}
founds_steps = []

def checkSquare(my_x, my_y, count, visited ):
    visited.append((my_x,my_y))
    found = {
        'left': (0,False),
        'right': (0,False),
        'up': (0,False),
        'down': (0, False),
    }
    
    if my_x == end_x and my_y == end_y:
        print(f"Found end with {count} steps")
        founds_steps.append(count)
        return (count, True)
    else:
        count += 1
        currValue = heightmap[(my_x,my_y)]
        if my_x > 0:
            left_delta = heightmap[(my_x-1,my_y)] - currValue
            if (0 <= left_delta <= 1) and (my_x-1,my_y) not in visited:
                print(f"on: {my_x},{my_y} looking left, count: {count} char: {alphabet[currValue]}")
                found['left'] = checkSquare(my_x-1,my_y, count, copy.deepcopy(visited))

        if my_x < width:
            right_delta = heightmap[(my_x+1,my_y)] - currValue
            if (0 <= right_delta <= 1) and (my_x+1,my_y) not in visited:
                print(f"on: {my_x},{my_y} looking right, count: {count} char: {alphabet[currValue]}")
                found['right'] = checkSquare(my_x+1,my_y, count, copy.deepcopy(visited))

        if my_y > 0:
            up_delta = heightmap[(my_x,my_y-1)] - currValue
            if (0 <= up_delta <= 1) and (my_x,my_y-1) not in visited:
                print(f"on: {my_x},{my_y} looking up, count: {count} char: {alphabet[currValue]}")
                found['up'] = checkSquare(my_x,my_y-1, count, copy.deepcopy(visited))

        if my_y < height:
            down_delta = heightmap[(my_x,my_y+1)] - currValue
            if (0 <= down_delta <= 1) and (my_x,my_y+1) not in visited:
                print(f"on: {my_x},{my_y} looking down, count: {count} char: {alphabet[currValue]}")
                found['down'] = checkSquare(my_x,my_y+1, count, copy.deepcopy(visited))

        lowest = ''
        for i in found.keys():
            if found[i][0] > 0 and found[i][1] == True and found[i][0] < found[lowest][0]:
                print(f"on: {my_x},{my_y} new lowest {i}")
                lowest = i
        
        if lowest == '':
            print(f"on: {my_x},{my_y} Dead end")
            return (1, False)
        else:
            print(f"on: {my_x},{my_y} returning shortest path")
            return found[lowest]


with open('input.txt') as input:
    while char := input.read(1):
        if str(char).isspace():
            x = 0
            y += 1
            continue
        elif char in alphabet:
            heightmap[(x,y)] = alphabet.index(char)
        elif char == 'S':
            print(f"found start at: {x},{y}")
            start_x = x
            start_y = y
            heightmap[(x,y)] = alphabet.index('a')
        elif char == 'E':
            print(f"found end at: {x},{y}")
            end_x = x
            end_y = y
            heightmap[(x,y)] = alphabet.index('z')
        else:
            print(char)
            print("oops")
        width = x
        x += 1

height = y
(steps, found) = checkSquare(start_x, start_y, 0, [])
print(f"minimum number of steps: {min(founds_steps)}")