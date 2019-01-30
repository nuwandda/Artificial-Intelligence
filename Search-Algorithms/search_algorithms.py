import csv
from collections import deque
from heapq import heappop, heappush


# Function that reads csv file and creates a list with the elements of csv file
def read_csv():
    with open('maze.csv', 'r') as f:
        reader = csv.reader(f)
        maze_2d = list(reader)
    return maze_2d


# Function that returns start and goal point of the given maze
def get_start_goal(maze):
    for i in maze:
        for j in i:
            if j == "S":
                start = (maze.index(i),i.index(j))
            elif j == "G":
                goal = (maze.index(i),i.index(j))
    return start, goal


# Function thst calculates the cost for given path.
# This function is written for to calculate the last and best paths for searches.
def calculate_cost(maze, path):
    cost = 0
    for i in path:
        x, y = i
        if maze[x][y] == "S":
            continue
        elif maze[x][y] == "G":
            cost = cost + 1
            continue
        else:
            cost = cost + int(maze[x][y])
            cost = cost + 1
    return cost


# Function that calculates the cost for UCS and A* algorithms.
# The difference is that this function takes care of extra move points.
def calculate_cost_ucs(maze, node):
    cost = 0
    without_extra_cost = 0
    x, y = node
    if maze[x][y] == "G":
        cost = cost + 1
        without_extra_cost = without_extra_cost + 1
    else:
        cost = cost + int(maze[x][y])
        without_extra_cost = without_extra_cost + 1
        cost = cost + 1
    return cost, without_extra_cost


# Function that returns neighbours for a given point inside the given maze.
def get_neighbours(point, maze):
    x,y = point
    border_x = len(maze)
    border_y = len(maze[0])
    temp_neighbours = [(x, y - 1), (x, y + 1), (x-1, y), (x+1, y)]
    neighbours = []
    for i in temp_neighbours:
        temp_x, temp_y = i
        if border_x > temp_x >= 0 and border_y > temp_y >= 0:
            neighbours.append(i)
    return neighbours


# Function that calculates the heuristic with Manhattan Distance Estimation.
# If the admissable is given False then it returns overestimated heuristic.
def heuristic(node, goal, admissable):
    if admissable:
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    else:
        return (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) * 10


# Function that does Breadth First Search
def bfs(maze, start, goal):
    frontier = deque([([start], start)])
    explored = set()

    while frontier:
        path, node = frontier.popleft()
        # Condition that checks if the search is finished.
        if node == goal:
            return "BFS path is: " + str(path) + "\nCost is: " + str(calculate_cost(maze, path))
        # If the node is already explored then it continues from other nodes.
        if node in explored:
            continue

        explored.add(node)
        neighbours = get_neighbours(node, maze)
        # Iterates over all the valid neighbours.
        for neighbour in neighbours:
            temp_x, temp_y = neighbour
            # Conditions that checks walls.
            if maze[temp_x][temp_y] != "-":
                frontier.append((path + [neighbour], neighbour))
    return "BFS: Failed"


# Function that does Depth First Search
def dfs(maze, start, goal):
    frontier = deque([([start], start)])
    explored = set()

    while frontier:
        path, node = frontier.pop()
        if node == goal:
            return "DFS path is: " + str(path) + "\nCost is: " + str(calculate_cost(maze, path))
        if node in explored:
            continue

        explored.add(node)
        neighbours = get_neighbours(node, maze)
        for neighbour in neighbours:
            temp_x, temp_y = neighbour
            if maze[temp_x][temp_y] != "-":
                frontier.append((path + [neighbour], neighbour))
    return "DFS: Failed"


def ucs(maze, start, goal, extra_move):
    frontier = []
    heappush(frontier, (0, [], start))
    explored = set()
    while frontier:
        cost, path, node = heappop(frontier)
        if node == goal:
            if extra_move:
                return "UCS path with extra move is: " + str(path) + "\nCost is: " + str(cost)
            else:
                return "UCS path without extra move is: " + str(path) + "\nCost is: " + str(calculate_cost(maze, path))

        if node in explored:
            continue

        explored.add(node)
        neighbours = get_neighbours(node, maze)
        for neighbour in neighbours:
            temp_x, temp_y = neighbour
            if neighbour not in explored:
                if maze[temp_x][temp_y] != "-":
                    # Temporary variables will be calculated for the calculation that is used without extra move points.
                    temp_cost, temp_without_extra_move = calculate_cost_ucs(maze, neighbour)
                    total_cost = cost + temp_cost
                    total_cost_without_extra = cost + temp_without_extra_move
                    # If the UCS is with extra move points, then it will be continued from if condition and will push
                    # the cost with extra move points.
                    if extra_move:
                        heappush(frontier, (total_cost, path + [neighbour], neighbour))
                    else:
                        heappush(frontier, (total_cost_without_extra, path + [neighbour], neighbour))

    return "UCS: Failed"


def astar(maze, start, goal, admissable):
    frontier = []
    heappush(frontier, (0 + heuristic(start, goal, True), 0, [], start))
    explored = set()
    while frontier:
        formula, cost, path, node = heappop(frontier)
        if node == goal:
            if admissable:
                return "Admissable A* path is: " + str(path) + "\nCost is: " + str(cost)
            else:
                return "Inadmissable A* path is: " + str(path) + "\nCost is: " + str(cost)

        if node in explored:
            continue

        explored.add(node)
        neighbours = get_neighbours(node, maze)
        for neighbour in neighbours:
            temp_x, temp_y = neighbour
            if neighbour not in explored:
                if maze[temp_x][temp_y] != "-":
                    temp_cost, temp_cost_without_extra = calculate_cost_ucs(maze, neighbour)
                    total_cost = cost + temp_cost
                    # If the flag will be given True, the frontier will be pushed a heuristic that is overestimated.
                    heappush(frontier, (total_cost + heuristic(neighbour, goal, admissable),
                                        total_cost, path + [neighbour], neighbour))
    return "A*: Failed"


if __name__ == '__main__':
    maze = read_csv()
    start, goal = get_start_goal(maze)

    bfs_solution = bfs(maze, start, goal)
    print(bfs_solution)

    dfs_solution = dfs(maze, start, goal)
    print(dfs_solution)

    # Param extra_move : True if calculating cost with extra move points.
    ucs_solution = ucs(maze, start, goal, True)
    print(ucs_solution)

    # Param admissable : True if calculating heuristic that is admissable.
    astar_solution = astar(maze, start, goal, True)
    print(astar_solution)
