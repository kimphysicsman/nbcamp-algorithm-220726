import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


# 거리 계산 함수
def distance(h_y, h_x, c_y, c_x):
    return abs(h_y - c_y) + abs(h_x - c_x)


# 최소 치킨거리 구하기 함수
def min_distance(homes, chickens, min_dist):
    total_dist = 0
    for home in homes:
        temp_dist_list = []
        for chicken in chickens:
            temp_dist = distance(home[0], home[1], chicken[0], chicken[1])
            temp_dist_list.append(temp_dist)
        total_dist += min(temp_dist_list)
    if min_dist > total_dist:
        min_dist = total_dist

    return min_dist



def get_min_city_chicken_distance(n, m, city_map):
    homes = []
    chickens = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                homes.append((i, j))
            elif city_map[i][j] == 2:
                chickens.append((i, j))

    min_dist = sys.maxsize

    del_num = len(chickens) - m
    if del_num > 0:
        del_list = list(itertools.combinations(chickens, del_num))
        for del_chickens in del_list:
            current_chickens = chickens.copy()
            for del_chicken in del_chickens:
                current_chickens.pop(del_chicken)
                min_dist = min_distance(homes, current_chickens, min_dist)
    else:
        min_dist = min_distance(homes, chickens, min_dist)

    return min_dist


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!