import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    all_count = []
    heap = []
    for i in range(2):
        for j in range(2):
            for h in range(2):
                all_count.append((i, j, h, i+j+h))

    for count in all_count:
        count_stock = stock
        able_bool = True

        for day in range(1, k+1):
            count_stock -= 1
            if count_stock < 0:
                able_bool = False
                break
            if day in dates:
                idx = dates.index(day)
                if count[idx]:
                    count_stock += supplies[idx]

        if able_bool:
            heapq.heappush(heap, count[3])

    return heapq.heappop(heap)


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))