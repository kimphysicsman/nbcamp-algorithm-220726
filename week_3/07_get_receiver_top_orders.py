top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    m = len(heights)
    orders = [0] * m
    for j in range(m):
        serve_tower = heights.pop()
        n = len(heights)
        for i in range(n):
            if heights[n-i-1] > serve_tower:
                orders[m-j-1] = n-i
                break

    return orders


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!