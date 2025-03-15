import time

# Constants
MAPWIDTH = 4
MAPHEIGHT = 5

STARTPOINT = [0, 2]
ENDPOINT = [1, 4]

checkpointList = [
        STARTPOINT,
        [0, 0],
        [1, 4],
        [3, 2],
        [3, 4],
        ENDPOINT
        ]

wallList = [ # Each of these walls' locations are based on their neighboring squares (Ex. wall #1 is between (2, 0) and (3, 0)
        [[2, 0], [3, 0]],
        [[1, 0], [1, 1]],
        [[3, 0], [3, 1]],
        [[0, 1], [0, 2]],
        [[0, 2], [1, 2]],
        [[2, 2], [3, 2]],
        [[1, 3], [1, 4]],
        [[3, 3], [3, 4]],
        [[1, 4], [2, 4]]
        ]

courseMap = []


def populateCourse(course, width, height):
    for x in range(width):
        for y in range(height):
            course.append([x, y])


def queryNeighbors(node):
    #           Right    Down    Left     Up
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in directions:  # for x in range(4)
        neighbor = [node[0] + dir[0], node[1] + dir[1]]  # [nodeX + DirectionModifierX, nodeY + DirectionModifierY]
        if neighbor in courseMap:  # Makes sure the neighbor is within bounds
            result.append(neighbor)
            for x in range(len(wallList)):
                if node in wallList[x] and neighbor in wallList[x]:  # TBD: Optimize determining if wall is present
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


def solveCourse(course, obstacles, checkpoints):
    stepsLength = 0
    courseDirections = ()

    for x in range(len(checkpoints) - 1):
        shortestPath = getShortestPath(course, checkpoints[x], checkpoints[x + 1])
        # if x != 0:
        #     del shortestPath[0]
        for i in range(len(shortestPath) - 1):
            diffX = shortestPath[i + 1][0] - shortestPath[i][0]
            if diffX == 1:
                courseDirections = courseDirections + (90, )
            elif diffX == -1:
                courseDirections = courseDirections + (270, )
            diffY = shortestPath[i + 1][1] - shortestPath[i][1]
            if diffY == 1:
                courseDirections = courseDirections + (180, )
            elif diffY == -1:
                courseDirections = courseDirections + (0, )
            stepsLength += 1
        print(shortestPath)
    print("Amount of steps: %d" % (stepsLength))
    print(courseDirections)


populateCourse(courseMap, MAPWIDTH, MAPHEIGHT)
solveCourse(courseMap, wallList, checkpointList)
