from collections import deque

# ฟังก์ชัน BFS เพื่อค้นหาเส้นทางที่สั้นที่สุด
def bfs(maze, start, end):
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    rows, cols = len(maze), len(maze[0])
    
    queue = deque([(start[0], start[1], 0, '')])  # แถว, คอลัมน์, ระยะทาง, เส้นทาง
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, dist, path = queue.popleft()
        
        if (x, y) == end:
            return path, dist
        
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == ' ' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1, path + direction))
    
    return None, -1  # หากหาเส้นทางไม่เจอ

# ฟังก์ชันหลัก
def solve_maze(maze):
    start = None
    end = None
    
    # หา start (X) และ end (Y)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'X':
                start = (i, j)
            elif maze[i][j] == 'Y':
                end = (i, j)
    
    if not start or not end:
        return "No start or end point"
    
    path, distance = bfs(maze, start, end)
    
    if distance == -1:
        return "No path found"
    
    time_taken = distance * 23  # เวลาในการวิ่ง (นาที)
    if time_taken <= 600:
        time_status = "You will make it on time!"
    else:
        time_status = "You won't make it on time."
    
    return path, distance, time_status

# รับ input ของวงกตจากผู้ใช้
def get_maze_input():
    print("Please input the maze (20x10 grid):")
    maze = []
    for i in range(10):  # วงกตขนาด 20x10
        row = input()
        if len(row) != 20:  # ตรวจสอบว่าความยาวของแต่ละแถวคือ 20
            print("Each row must be exactly 20 characters.")
            return None
        maze.append(list(row))
    return maze

# เรียกใช้ฟังก์ชันรับ input และแก้ปัญหา
maze = get_maze_input()

if maze:
    result = solve_maze(maze)
    
    # แสดงผลลัพธ์
    if isinstance(result, tuple):
        print(result[0])  # เส้นทาง
        print(result[1])  # ระยะทาง
        print(result[2])  # สถานะเวลา
    else:
        print(result)
