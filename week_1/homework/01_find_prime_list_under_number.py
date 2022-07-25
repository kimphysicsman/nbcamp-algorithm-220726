input = 20


def find_prime_list_under_number(number):
    if number < 2:
        return []

    prime_list = [2]

    for num in range(2, number+1):
        prime_bool = True
        for prime in prime_list:
            if num % prime == 0:
                prime_bool = False
                break
        if prime_bool:
            prime_list.append(num)

    return prime_list


result = find_prime_list_under_number(input)
print(result)