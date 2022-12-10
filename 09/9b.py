NUM_KNOTS = 10

# a class to model the rope of knots
class Knot:
    def __init__(self, upstreamKnot, id):
        self.upstreamKnot = upstreamKnot
        self.id = id
        self.x = 0
        self.y = 0
        self.grid = {(self.x,self.y): True}
        print(f"I'm Knot id:{id}")

    def move(self, direction):
        # i.e. we're the head, so we just move accordingly
        if self.upstreamKnot == None:
            if direction == 'L':
                self.x -= 1
            elif direction == 'R':
                self.x += 1
            elif direction == 'U':
                self.y -= 1
            elif direction == 'D':
                self.y += 1
        # we're a knot behind, so we check upstream and move accordingly
        else:
            y_adj = self.upstreamKnot.y - self.y 
            x_adj = self.upstreamKnot.x - self.x
            
            if abs(y_adj) > 1:
                if y_adj > 0: self.y += 1
                else: self.y -= 1
                if self.x != self.upstreamKnot.x:
                    if x_adj > 0: self.x += 1
                    else: self.x -= 1

            elif abs(x_adj) > 1:
                if x_adj > 0: self.x += 1
                else: self.x -= 1
                if self.y != self.upstreamKnot.y:
                    if y_adj > 0: self.y += 1
                    else: self.y -= 1
        
        # track where we've been
        self.grid[(self.x,self.y)] = True
        #print(f"Knot ID: {self.id} now at: {self.x},{self.y}")

with open('input.txt') as input:
    data = []
    while line := input.readline().strip():
        direction, count = line.split()
        data.append((direction, int(count)))
    
    # create our rope of knots
    rope = []
    rope.append(Knot(None, 'H')) # our head)
    for knot in range(1,NUM_KNOTS):
            rope.append(Knot(rope[knot-1], knot))
    
    # move
    for (direction,count) in data:
        #print(f"moving: {direction}{count}")
        for x in range(count):
            #print(f"--- step {x+1} ---")
            for knot in rope:
                knot.move(direction)
            
    print(f"number of positions visited by the tail: {len(rope[-1].grid.keys())}")