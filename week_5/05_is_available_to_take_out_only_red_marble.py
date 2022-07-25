from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 왼 / 아래 / 오른쪽 / 위
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


# 현재 좌표에서 i 방향으로 기울였을 때 좌표
def move_one_count(y, x, i, game_map):
    count = 0
    while True:
        count += 1
        y += dy[i]
        x += dx[i]
        if game_map[y][x] == "#":
            break
        elif game_map[y][x] == "O":
            break
    return y, x, count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])

    queue = deque()
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

    red_y, red_x, blue_y, blue_x = None, None, None, None

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_y, red_x = i, j
            if game_map[i][j] == "B":
                blue_y, blue_x = i, j

    queue.append((red_y, red_x, blue_y, blue_x, 0))
    visited[red_y][red_x][blue_y][blue_x] = True

    while queue:
        red_y, red_x, blue_y, blue_x, count = queue.popleft()
        if count > 10:
            break

        for i in range(4):
            next_r_y, next_r_x, r_count = move_one_count(red_y, red_x, i, game_map)
            next_b_y, next_b_x, b_count = move_one_count(blue_y, blue_x, i, game_map)

            if game_map[next_b_y][next_b_x] == "O":
                continue
            if game_map[next_r_y][next_r_x] == "O":
                return True
            if next_r_y == next_b_y and next_r_x == next_b_x:
                if r_count > b_count:
                    next_r_y -= dy[i]
                    next_r_x -= dx[i]
                else:
                    next_b_y -= dy[i]
                    next_b_x -= dx[i]

            if not visited[next_r_y][next_r_x][next_b_y][next_b_x]:
                visited[next_r_y][next_r_x][next_b_y][next_b_x] = True
                queue.append((next_r_y, next_r_x, next_b_y, next_b_x, count+1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다