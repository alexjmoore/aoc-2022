with open('input.txt') as input:
    data = []
    while line := input.readline().strip():
        data.append([int(d) for d in str(line)])

    rows = len(data[0])
    columns = len(data)
    visible_count = 0
    max_score = 0
    
    for y in range(1,columns-1):
        for x in range(1,rows-1):
            curr = data[y][x]
            visible = True
            visible_up = True
            visible_down = True
            visible_left = True
            visible_right = True
            
            score_up = 0
            score_down = 0
            score_left = 0
            score_right = 0

            for i in range(1,max(rows,columns)-1):       
                if ((y-i) >= 0) and (data[y-i][x] >= curr) and visible_up:
                    score_up += 1
                    visible_up = False                    
                                  
                if ((y+i) < columns) and (data[y+i][x] >= curr) and visible_down:
                    score_down += 1
                    visible_down = False

                if ((x-i) >= 0)  and (data[y][x-i] >= curr) and visible_left:
                    score_left += 1
                    visible_left = False
                
                if ((x+i) < rows) and (data[y][x+i] >= curr) and visible_right:
                    score_right += 1
                    visible_right = False

                if not any([visible_up,visible_down,visible_left,visible_right]):
                    visible = False
                    break
                
                if ((y-i) >= 0) and visible_up: score_up+=1
                if ((y+i) < columns) and visible_down: score_down+=1
                if ((x-i) >= 0) and visible_left: score_left+=1
                if ((x+i) < rows) and visible_right: score_right+=1

            if visible == True:
                visible_count += 1
            total_score = score_up * score_down * score_left * score_right
            max_score = max(max_score, total_score)
                
    perim_trees = (rows * 2) + (columns * 2) - 4
    print(f"perimerter trees: {perim_trees}, visible trees: {visible_count}")
    print(f"total visible tree: {perim_trees + visible_count}")
    print(f"max scenic score: {max_score}")