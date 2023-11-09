string1 = "()[]{}"

brackets = {
    '{': '}',
    '(': ')',
    '[':']'
}

stack = []
def valparen(str1):

    for item in str1:
        if item in brackets:
            stack.append(item)
        elif len(stack) == 0 or item!= brackets[stack.pop()]:
            return False
    return len(stack) == 0

print(valparen(string1))

