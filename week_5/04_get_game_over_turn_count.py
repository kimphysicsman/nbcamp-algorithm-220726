k = 4  # 말의 개수

chess_map = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]
start_horse_location_and_directions = [
    [1, 0, 0],
    [2, 1, 2],
    [1, 1, 0],
    [3, 0, 1]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!

#     2
#
# 1       0
#
#     3


# d를 반대 방향으로 변경
def reverse_d(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2


# 현재 좌표에 따른 한칸 이동한 후의 좌표
def move_one_count(y, x, d):
    if d == 0:
        x = x + 1
    elif d == 1:
        x = x - 1
    elif d == 2:
        y = y - 1
    else:
        y = y + 1

    return y, x, d


# game_map과 말들의 좌표를 입력받아
# 외곽을 2로 설정한 wall_map과 해당 map의 좌표로 변환
def wall_map(game_map, horse_location_and_directions):
    n = len(game_map)
    new_map = [[2 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_map[i + 1][j + 1] = game_map[i][j]

    for i in range(len(horse_location_and_directions)):
        horse_location_and_directions[i][0] += 1
        horse_location_and_directions[i][1] += 1

    return new_map, horse_location_and_directions


# 실재로 맵 이동
# i번 째 말이 현재 pre_position 좌표에서 이동 후 겹친 말 개수 변환
def move_func(i, pre_position, new_map, horse_status, new_location):
    pre_y, pre_x, d = pre_position
    # 이동할 좌표
    y, x, d = move_one_count(pre_y, pre_x, d)

    # 이동할 좌표가 흰색 또는 적색이면 겹친 말들과 이동
    if new_map[y][x] == 0 or new_map[y][x] == 1:
        for idx, j in enumerate(horse_status[pre_y][pre_x]):
            if j == i:
                move_horse = horse_status[pre_y][pre_x][idx:]
                horse_status[pre_y][pre_x] = horse_status[pre_y][pre_x][:idx]
                break
        for num in move_horse:
            new_location[num][0] = y
            new_location[num][1] = x

        # 이동한 좌표가 흰색이면 해당 좌표의 말 상태에 그대로 추가
        if new_map[y][x] == 0:
            horse_status[y][x].extend(move_horse)

        # 이동한 좌표가 적색이면 해당 좌표의 말 상태에 역순으로 추가
        else:
            for _ in range(len(move_horse)):
                horse_status[y][x].append(move_horse.pop())

    # 이동할 좌표가 청색이면 이동방향을 반대로 변경한 후 이동
    else:
        # 방향 변경
        d = reverse_d(d)

        # 반대 방향도 파란색이 아닐 경우 이동
        y, x, d = move_one_count(pre_y, pre_x, d)
        if new_map[y][x] != 2:
            pre_position[2] = d
            move_func(i, pre_position, new_map, horse_status, new_location)

    return len(horse_status[y][x])


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    count = 0

    # 외곽을 2로 감싼 새로운 맵과 좌표
    new_map, new_location = wall_map(game_map, horse_location_and_directions)

    n = len(game_map)

    # 좌표별 말 위치 상태
    horse_status = dict()
    for y in range(1, n + 1):
        horse_status[y] = dict()
        for x in range(1, n + 1):
            horse_status[y][x] = list()

    for i, (y, x, d) in enumerate(new_location):
        horse_status[y][x].append(i)

    # print("-------")
    # print(count)
    # for i in range(1, len(horse_status)+1):
    #     print(horse_status[i])

    while True:
        # 턴 진행
        count += 1
        if count > 1000:
            break

        for i in range(horse_count):
            # i번째 말 이동

            # 현재 말 좌표
            pre_position = new_location[i]

            # 이동 함수 및 이동 후 겹친 말 개수 반환
            horse_num = move_func(i, pre_position, new_map, horse_status, new_location)

        if horse_num >= 4:
            return count

        # if count > 5:
        #     break
        # else:
        #     print("-------")
        #     print(count)
        #     for i in range(len(horse_status)):
        #         print(horse_status[i + 1])

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
