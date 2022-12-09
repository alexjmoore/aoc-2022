DIST = 9
with open('test_input2.txt') as input:
    data = []
    while line := input.readline().strip():
        direction, count = line.split()
        data.append((direction, int(count)))
    
    h_pos_x = h_pos_y = t_pos_x = t_pos_y = 0
    
    # our starting (and visited) position
    grid = {(t_pos_x,t_pos_y): True}
    for (direction,count) in data:
        print(f"moving: {direction}{count}")
        for x in range(count):
            if direction == 'L':
                h_pos_x -= 1
            elif direction == 'R':
                h_pos_x += 1
            elif direction == 'U':
                h_pos_y -= 1
            elif direction == 'D':
                h_pos_y += 1
            
            y_adj = h_pos_y - t_pos_y 
            x_adj = h_pos_x - t_pos_x

            if abs(y_adj) > DIST:
                if y_adj > 0: t_pos_y += 1
                else: t_pos_y -= 1
                if t_pos_x != h_pos_x:
                    if x_adj > 0: t_pos_x += 1
                    else: t_pos_x -= 1
            if abs(x_adj) > DIST:
                if x_adj > 0: t_pos_x += 1
                else: t_pos_x -= 1
                if t_pos_y != h_pos_y:
                    if y_adj > 0: t_pos_y += 1
                    else: t_pos_y -= 1
            
            print(f"tail: {t_pos_x},{t_pos_y} head: {h_pos_x},{h_pos_y}")
            print(f"x_adj: {x_adj} y_adj: {y_adj}")
            grid[(t_pos_x,t_pos_y)] = True
            
    print(f"number of positions visited by the tail: {len(grid.keys())}")