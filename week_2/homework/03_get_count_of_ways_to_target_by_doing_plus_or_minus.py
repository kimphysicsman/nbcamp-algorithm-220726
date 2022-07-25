numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    print(array, target)
    if len(array) == 1:
        if array[0] == target or -1 * array[0] == target:
            return 1
        else:
            return 0

    last = array[-1]
    target_1 = target + last
    target_2 = target - last

    way_1 = get_count_of_ways_to_target_by_doing_plus_or_minus(array[:-1], target_1)
    way_2 = get_count_of_ways_to_target_by_doing_plus_or_minus(array[:-1], target_2)

    return way_1 + way_2

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!