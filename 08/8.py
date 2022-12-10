with open('input.txt') as input:
    data = []
    while line := input.readline().strip():
        data.append([int(d) for d in str(line)])

    rows = len(data[0])
    columns = len(data)
    visible_count = 0

    for y in range(1,columns-1):
        for x in range(1,rows-1):
            curr = data[y][x]
            visible = True
            visible_up = True
            visible_down = True
            visible_left = True
            visible_right = True
            
            for i in range(1,max(rows,columns)-1):       
                if ((y-i) >= 0) and (data[y-i][x] >= curr) and visible_up:
                    visible_up = False                    
                                  
                if ((y+i) < columns) and (data[y+i][x] >= curr) and visible_down:
                    visible_down = False

                if ((x-i) >= 0)  and (data[y][x-i] >= curr) and visible_left:
                    visible_left = False
                
                if ((x+i) < rows) and (data[y][x+i] >= curr) and visible_right:
                    visible_right = False

                if not any([visible_up,visible_down,visible_left,visible_right]):
                    visible = False
                    break

            if visible == True:
                visible_count += 1
                
    perim_trees = (rows * 2) + (columns * 2) - 4
    print(f"perimeter trees: {perim_trees}, visible trees: {visible_count}")
    print(f"total visible tree: {perim_trees + visible_count}")