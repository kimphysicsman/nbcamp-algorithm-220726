import pprint

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 현재 d를 기준으로 num번 회전
def rotation_d(d, num):
    for _ in range(num):
        d = d - 1
        if d < 0:
            d = 3
    return d


# 현재 r, c, d를 기준으로 좌표 변환
def transform_rc(r, c, d):
    if d == 0:
        return r-1, c
    if d == 1:
        return r, c+1
    if d == 2:
        return r+1, c
    if d == 3:
        return r, c-1

#     0
#
# 3       1
#
#     2

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    count = 1
    room_map[r][c] = count+1
    while True:
        # 현재 r, c, d를 기준으로 (왼쪽, 뒤, 오른쪽, 바라보는방향)
        all_dir = [rotation_d(d, 1), rotation_d(d, 2), rotation_d(d, 3), d]
        positions = [transform_rc(r, c, d) for d in all_dir]
        positions = [room_map[i][j] for i, j in positions]

        if positions[1] == 1 and 0 not in positions:
            break
        elif 0 not in positions:
            r, c = transform_rc(r, c, rotation_d(d, 2))
        else:
            for i, pos in enumerate(positions):
                if pos == 0:
                    d = all_dir[i]
                    r, c = transform_rc(r, c, d)
                    count += 1
                    room_map[r][c] = count+1
                    break
    return count

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))