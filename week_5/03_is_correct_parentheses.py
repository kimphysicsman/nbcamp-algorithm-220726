from collections import deque

balanced_parentheses_string = "()))((()"
a = "(()())()"	# -> "(()())()"
b = ")("        # -> "()"
c = "()))((()"	# -> "()(())()"


def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""

    # 문자열 나누기
    correct_bool = True
    count = 0
    pos = 0
    for i, char in enumerate(balanced_parentheses_string):
        if char == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            correct_bool = False
        if count == 0:
            pos = i
            break

    u = balanced_parentheses_string[:pos+1]
    v = balanced_parentheses_string[pos+1:]

    # 올바른 괄호 문자열인지 확인
    if correct_bool:
        return u + get_correct_parentheses(v)
    else:
        string = "(" + get_correct_parentheses(v) + ")"

        u = u[1:-1]
        queue = deque()
        for i, char in enumerate(u):
            if char == "(":
                queue.append(")")
            else:
                queue.append("(")
        transform_u = ""
        for _ in range(len(queue)):
            transform_u += queue.popleft()

        return string + transform_u


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
print(get_correct_parentheses(a))
print(get_correct_parentheses(b))
print(get_correct_parentheses(c))