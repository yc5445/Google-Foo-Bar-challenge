def bfs(sx, sy, maze):
    h, w = len(maze), len(maze[0])
    board = [[None] * w for _ in range(h)]
    board[sx][sy] = 1
    arr = [(sx, sy)]

    while arr:
        x, y = arr.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if maze[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))
    return board

def solution(maze):
    h, w = len(maze), len(maze[0])
    tb = bfs(0, 0, maze)
    bt = bfs(h-1, w-1, maze)
    ans = float("inf")

    for i in range(h):
        for j in range(w):
            if tb[i][j] and bt[i][j]:
                ans = min(ans, tb[i][j] + bt[i][j] - 1)
    return ans

if __name__ == "__main__":
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
