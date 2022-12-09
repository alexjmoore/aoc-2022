with open('input.txt') as input:
    data = []
    while line := input.readline().strip():
        direction, count = line.split()
        data.append((direction, int(count)))
    
    h_pos_x = h_pos_y = t_pos_x = t_pos_y = 0
    
    # our starting (and visited) position
    grid = {(t_pos_x,t_pos_y): True}
    for (direction,count) in data:
        for x in range(count):
            if direction == 'L':
                h_pos_x -= 1
                if abs(h_pos_x - t_pos_x) > 1:
                    t_pos_x -= 1
                    t_pos_y = h_pos_y
            elif direction == 'R':
                h_pos_x += 1
                if abs(h_pos_x - t_pos_x) > 1:
                    t_pos_x += 1
                    t_pos_y = h_pos_y
            elif direction == 'U':
                h_pos_y -= 1
                if abs(h_pos_y - t_pos_y) > 1:
                    t_pos_y -= 1
                    t_pos_x = h_pos_x
            elif direction == 'D':
                h_pos_y += 1
                if abs(h_pos_y - t_pos_y) > 1:
                    t_pos_y += 1
                    t_pos_x = h_pos_x
            grid[(t_pos_x,t_pos_y)] = True
            
    print(f"number of positions visited by the tail: {len(grid.keys())}")