shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def bubble_sort(array):
    while True:
        sort_bool = True
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort_bool = False
        if sort_bool:
            break

    return array


def selection_sort(array):
    n = len(array)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if array[j] > array[max_index]:
                max_index = j
            array[i], array[max_index] = array[max_index], array[i]

    return array


def insertion_sort(array):
    new_array = [array[0]]
    n = len(array)
    for i in range(1, n):
        new_array.append(array[i])
        m = len(new_array)
        for j in range(m-1, 1, -1):
            if new_array[j] > new_array[j-1]:
                new_array[j], new_array[j-1] = new_array[j-1], new_array[j]
            else:
                break

    return array


def insertion_sort_2(array):
    for i in range(len(array)):
        for j in range(i):
            index = i - j - 1
            if array[index+1] > array[index]:
                array[index], array[index+1] = array[index+1], array[index]
            else:
                break
    return array


def get_max_discounted_price(prices, coupons):
    prices = insertion_sort_2(prices)
    coupons = insertion_sort_2(coupons)

    index = 0
    result = 0

    while True:
        if index >= len(prices):
            break
        if index >= len(coupons):
            for i in range(index, len(prices)):
                result += prices[i]
            break

        result += prices[index] * (1 - coupons[index] / 100)
        index += 1

    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.