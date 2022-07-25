from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    count = 0

    queue = deque()
    queue.append(brown_loc)

    while True:
        # 하루 추가
        count += 1

        # 코니 위치
        cony_loc += count

        # 브라운이 위치를 저장할 곳
        visited = dict()

        # 브라운 위치 저장
        len_queue = len(queue)
        for _ in range(len_queue):
            # 전날 브라운 위치에 따른 다음 위치 저장
            pre_brown_loc = queue.popleft()

            brown_loc = pre_brown_loc - 1
            if 0 <= brown_loc <= 200000 and brown_loc not in visited:
                queue.append(brown_loc)
                visited[brown_loc] = 1

            brown_loc = pre_brown_loc + 1
            if 0 <= brown_loc <= 200000 and brown_loc not in visited:
                queue.append(brown_loc)
                visited[brown_loc] = 1

            brown_loc = pre_brown_loc * 2
            if 0 <= brown_loc <= 200000 and brown_loc not in visited:
                queue.append(brown_loc)
                visited[brown_loc] = 1

        if not 0 <= cony_loc <= 200000:
            break

        if cony_loc in visited:
            return count

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))