seat_count = 9
vip_seat_array = [4, 7]

count = 0


def temp(seat, graph, n):
    global count
    if n > 9:
        count += 1
        # print(n, seat, count)
        return
    seats = list()
    for i in graph[n]:
        seat_bool = False
        new_seat = seat.copy()
        if i not in new_seat:
            new_seat.append(i)
            seat_bool = True
        if seat_bool:
            seats.append(new_seat)
    for s in seats:
        temp(s, graph, n+1)


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    graph = {}
    for i in range(1, total_count+1):
        graph[i] = list()
        if i not in fixed_seat_array:
            seats = [i-1, i, i+1]
            for seat in seats:
                if 0 < seat < total_count+1 and seat not in fixed_seat_array:
                    graph[i].append(seat)
        else:
            graph[i].append(i)

    # print(graph)

    seat = []
    temp(seat, graph, 1)

    return count



# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))