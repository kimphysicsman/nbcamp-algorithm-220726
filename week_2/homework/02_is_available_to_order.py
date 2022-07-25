shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    shop_menus.sort()
    order_bool = True

    for order in shop_orders:
        order_bool = order_bool & find_binary_by_recursion(shop_menus, order, 0, len(shop_menus)-1)

    return order_bool


def find_binary_by_recursion(array, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if target == array[mid]:
        return True
    if target < array[mid]:
        return find_binary_by_recursion(array, target, start, mid-1)
    else:
        return find_binary_by_recursion(array, target, mid+1, end)


result = is_available_to_order(shop_menus, shop_orders)
print(result)