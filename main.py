mapWidth = 4
mapHeight = 5
startPos = [0, 2]
endPos = [1, 4]

checkpointList = [
        startPos,
        [0, 0],
        [1, 4],
        [3, 2],
        [3, 4],
        endPos
        ]

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

courseMap = []
for x in range(mapWidth): # Like for(int x = 0; x > 20; i++) {
    for y in range(mapHeight):
        courseMap.append([x, y])

def queryNeighbors(node):
#                 Right    Down    Left     Up
    directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in directions: # Basically for x in range(4)
        neighbor = [node[0] + dir[0], node[1] + dir[1]] # [nodeX + DirectionModifierX, nodeY + DirectionModifierY]
        if neighbor in courseMap: # If neighbor is present in the grid:
            result.append(neighbor)
            for x in range(len(obstacleList)):
                if node in obstacleList[x] and neighbor in obstacleList[x]:
                    result.remove(neighbor)
    return result

def getShortestPath(courseMap, startPos, endPos):
    searchPaths = [[startPos]]
    visitedCoordinates = [startPos]

    while searchPaths != []:
        currentPath = searchPaths.pop(0)
        currentPos = currentPath[-1]

        if currentPos == endPos:
            return currentPath

        for nextPos in queryNeighbors(currentPos):
            if nextPos in visitedCoordinates:
                continue
            searchPaths.append(currentPath + [nextPos])
            visitedCoordinates += nextPos

def solveCourse(courseMap, obstacleList, checkpointList):
    for x in range(len(checkpointList) - 1): # Repeat 6 Times
        shortestPath = getShortestPath(courseMap, checkpointList[x], checkpointList[x + 1])
        print(shortestPath)
    
solveCourse(courseMap, obstacleList, checkpointList)


