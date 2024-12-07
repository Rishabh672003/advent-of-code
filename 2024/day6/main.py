directions = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}


def get_start(text: list[str]) -> tuple[int, int]:
    for i in range(len(text)):
        for j in range(len(text[0])):
            if maze[i][j] == "^":
                return (i, j)
    return (-1, -1)


def part1(start: tuple[int, int], maze: list[str]):
    i, j = start
    dir = "up"
    ROW, COLUMN = len(maze) - 1, len(maze[0]) - 1
    tracer: list[list[str|None]] = [[None for _ in range(ROW + 1)] for _ in range(COLUMN + 1)]
    count = 0
    while i != 0 and j != 0 and i != ROW and j != COLUMN:
        if not tracer[i][j]:
            count += 1
            tracer[i][j] = "visited"
        else:
            print(i, j, "visited")
        if dir == "up":
            if i > 0 and maze[i - 1][j] != "#":
                i -= 1
            else:
                dir = "right"
        elif dir == "right":
            if j < COLUMN and maze[i][j + 1] != "#":
                j += 1
            else:
                dir = "down"
        elif dir == "down":
            if i < ROW and maze[i + 1][j] != "#":
                i += 1
            else:
                dir = "left"
        elif dir == "left":
            if j > 0 and maze[i][j - 1] != "#":
                j -= 1
            else:
                dir = "up"
        
    print(count+1)

# def part2(start: tuple[int, int], maze: list[str]):
#     ROW, COLUMN = len(maze), len(maze[0])
#     count = 0
#     sum = 0
#     delta = [(0, -1), (1,0), (0, 1), (-1, 0)]
#     obstacles: set[tuple[int, int]] = set()
#     empty_pos: set[tuple[int, int]]= set()
#     for i in range(ROW):
#         for j in range(COLUMN):
#             if maze[i][j] == "#":
#                 obstacles.add((i, j))
#             elif maze[i][j] == "^":
#                 start = (i, j)
#             else:
#                 empty_pos.add((i, j))
#     possible_places = empty_pos
#     for i in possible_places:
#         cur_obstacle = obstacles.copy()
#         cur_obstacle.add(i)
#         guard_pos = start
#         seen_states = set()
#         while True:
#             x,y = guard_pos
#             if 0 > x >= COLUMN or 0 > y >= ROW:
#                 break
#             state = (guard_pos)
#
#     print(sum)


def part2(start: tuple[int, int], maze: list[str]):
    start_i, start_j = start
    print(start)
    dir = "up"
    ROW, COLUMN = len(maze) - 1, len(maze[0]) - 1
    tracer: list[list[str|None]] = [[None for _ in range(COLUMN + 1)] for _ in range(ROW + 1)]
    count = 0
    maze = [list(row) for row in maze]
    
    for i in range(ROW + 1):
        for j in range(COLUMN + 1):
            visited = set()
            print(i, visited, start_i)
            start_i, start_j = start
            if maze[i][j] != "#" and maze[i][j] != "^":
                maze[i][j] = "#"
            while 0 < start_i < ROW and 0 < start_j < COLUMN:
                if dir == "up":
                    if start_i > 0 and maze[start_i - 1][start_j] != "#":
                        start_i -= 1
                        if (start_i, start_j, "up") in visited:
                            count +=1
                            break
                        visited.add((start_i, start_j, "up"))
                    else:
                        dir = "right"
                elif dir == "right":
                    if start_j < COLUMN and maze[start_i][start_j + 1] != "#":
                        start_j += 1
                        if (start_i, start_j, "right") in visited:
                            count +=1
                            break
                        visited.add((start_i, start_j, "right"))
                    else:
                        dir = "down"
                elif dir == "down":
                    if start_i < ROW and maze[start_i + 1][start_j] != "#":
                        start_i += 1
                        if (start_i, start_j, "down") in visited:
                            count +=1
                            break
                        visited.add((start_i, start_j, "down"))
                    else:
                        dir = "left"
                elif dir == "left":
                    if start_j > 0 and maze[start_i][start_j - 1] != "#":
                        start_j -= 1
                        if (start_i, start_j, "left") in visited:
                            count +=1
                            break
                        visited.add((start_i, start_j, "left"))
                    else:
                        dir = "up"
        
    print(count)


if __name__ == "__main__":
    maze: list[str] = []
    with open("2024/day6/input.txt") as file:
        for i in file:
            maze.append(i.strip())

    initial_pos = get_start(maze)
    # part1(initial_pos, maze)

    part2(initial_pos, maze)
