import numpy as np

# x---x---x---x---x
# |           |   |
# | A         |   |
# |           |   |
# x   x---x   x---x
# |               |
# |               |
# |               |
# x---x       x   x
# |   |       |   |
# S   |       | C |
# |   |       |   |
# x   x       x   x
# |               |
# |               |
# |               |
# x   x---x   x---x
# |       |       |
# |     B |     D |
# |     L |       |
# x---x---x---x---x

mapWidth = 4
mapHeight = 5
currentPos = [2, 2]

allNodes = []
for x in range(mapWidth): # Like for(int x = 0; x > 20; i++) {
    for y in range(mapHeight):
        allNodes.append([x, y])

def queryNeighbors(node, obstacleList):
#                 Right    Down    Left     Up
    directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in directions: # Basically for x in range(4)
        neighbor = [node[0] + dir[0], node[1] + dir[1]] # [nodeX + DirectionModifierX, nodeY + DirectionModifierY]
        if neighbor in allNodes: # If neighbor is present in the grid:
            result.append(neighbor)
            for x in range(len(obstacleList)):
                if node in obstacleList[x] and neighbor in obstacleList[x]:
                    result.remove(neighbor)
    return result

obstacleList = [
        [[2, 0], [3, 0]], # obstacleList[0]
        [[1, 0], [1, 1]], # obstacleList[1]
        [[3, 0], [3, 1]],
        [[0, 1], [0, 2]],
        [[0, 2], [1, 2]],
        [[2, 2], [3, 2]],
        [[1, 3], [1, 4]],
        [[3, 3], [3, 4]],
        [[1, 4], [2, 4]]
        ]

# print('OBSTACLES:')
# for x in range(len(obstacleList)):
#     print(obstacleList[x])
print('CURRENT POSITION:')
print(currentPos)
print('NEIGHBORS:')
print(queryNeighbors(currentPos, obstacleList))

