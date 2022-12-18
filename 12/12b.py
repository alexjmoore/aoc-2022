import string, copy, sys, math
from dataclasses import dataclass
from typing import Optional

ALPHABET = list(string.ascii_lowercase)
nodes = {}
x = y = 0
start = end = None

@dataclass
class Node:
    x: int
    y: int
    value: int
    neighbours: list[(int,int)]
    distance: Optional[float] = math.inf

def isValidNeighbour(currNode, targetNode):
    if targetNode.value - currNode.value <= 1: return True
    return False

startChoices = []
with open('input.txt') as input:
    while char := input.read(1):
        node = None
        if str(char).isspace():
            x = 0
            y += 1
            continue
        elif char in ALPHABET:
            if char == 'a':
                startChoices.append((x,y))
                node = Node(x, y, ALPHABET.index(char), [], distance = 0)
            else:
                node = Node(x, y, ALPHABET.index(char), [])
        elif char == 'S':
            startChoices.append((x,y))
            start = node = Node(x, y, 0, [], distance=0)   
        elif char == 'E':
            end = node = Node(x, y, ALPHABET.index('z'), [])
        nodes[(x, y)] = node
        x += 1

# build our graph
width = max(list(nodes.keys()))[0]
height = max(list(nodes.keys()))[1]
for i in range(width+1):
    for j in range(height+1):
        if i > 0:
            if isValidNeighbour(nodes[(i,j)],nodes[(i-1, j)]):
                nodes[(i, j)].neighbours.append((i-1, j))
        if i < width:
            if isValidNeighbour(nodes[(i,j)],nodes[(i+1, j)]):
                nodes[(i, j)].neighbours.append((i+1, j))
        if j > 0:
            if isValidNeighbour(nodes[(i,j)],nodes[(i, j-1)]):
                nodes[(i, j)].neighbours.append((i, j-1))
        if j < height:
            if isValidNeighbour(nodes[(i,j)],nodes[(i, j+1)]):
                nodes[(i, j)].neighbours.append((i, j+1))

print(f"found start at: {start.x},{start.y} and end at: {end.x},{end.y}")
unvisited = copy.deepcopy(nodes)

allSteps = []
while len(unvisited) > 0:
    shortest = min(unvisited, key=lambda x: unvisited[x].distance)
    updateNode = unvisited.pop(shortest)

    print(f"c: {updateNode.x+1},{updateNode.y+1} d: {updateNode.distance}")
    if (updateNode.x == end.x) and (updateNode.y == end.y):
            print(f"found end! {updateNode.distance}")
            allSteps.append(updateNode.distance)
    distance = updateNode.distance + 1
    for (nx, ny) in updateNode.neighbours:     
        if (nx, ny) in unvisited.keys():
            if distance < unvisited[(nx, ny)].distance:
                unvisited[(nx, ny)].distance = distance
                print(f"|--- n: {unvisited[(nx,ny)].x+1},{unvisited[(nx, ny)].y+1} d: {unvisited[(nx, ny)].distance}")

print(f"minimum number of steps: {allSteps}")