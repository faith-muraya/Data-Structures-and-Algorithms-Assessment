def is_balanced(expression):
    stack = []
    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            else:
                opening_bracket = stack.pop()
                closing_bracket = closing_brackets[opening_brackets.index(opening_bracket)]
                if char != closing_bracket:
                    return False

    return len(stack) == 0