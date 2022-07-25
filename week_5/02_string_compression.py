input = "abcabcabcabcdededededede"
a = "aabbaccc"	# -> 7
b = "ababcdcdababcdcd"	# -> 9
c = "abcabcdede"	# -> 8
d = "abcabcabcabcdededededede"	# -> 14
e = "xababcdcdababcdcd"	# -> 17



def string_compression(string):
    len_string = len(string)

    len_min = len_string

    for i in range(1, len_string//2 + 1):
        # i : 자르는 단위
        # string을 앞에서부터 자르면서 stack에 넣는데 stack head와 같으면 않넣고 count를 +1
        stack = []

        for j in range(len_string//i + 1):
            # 자르는 위치
            pos_start = j * i
            pos_end = j * i + i

            if pos_end > len_string + 1:
                word = string[pos_start:]
            else:
                word = string[pos_start:pos_end]

            if word == "":
                pass
            elif len(word) < i:
                stack.append([word, 1])
            elif len(stack) == 0:
                stack.append([word, 1])
            elif stack[-1][0] == word:
                stack[-1][1] += 1
            else:
                stack.append([word, 1])

        result_string = ""
        for word, count in stack:
            if count > 1:
                result_string += str(count) + word
            else:
                result_string += word

        if len_min > len(result_string):
            len_min = len(result_string)

    return len_min


print(string_compression(input))  # 14 가 출력되어야 합니다!
print(string_compression(a))  # 7 가 출력되어야 합니다!
print(string_compression(b))  # 9 가 출력되어야 합니다!
print(string_compression(c))  # 8 가 출력되어야 합니다!
print(string_compression(d))  # 14 가 출력되어야 합니다!
print(string_compression(e))  # 17 가 출력되어야 합니다!