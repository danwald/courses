def check_valid(ops):
    '''checks if the input string has balanced opertaors'''
    stack = []
    try:
        for o in ops:
            if o in '[{(':
                stack.append(o)
                continue
            elif o in ']})':
                vl = stack.pop()
                if (vl,o,) in set( [('[', ']'), ('{', '}'), ('(', ')')]):
                    continue
            raise ValueError
    except:
        return False
    return False if len(stack) else True


if __name__ == '__main__':
    test_cases = (
        ('[[[]]]', True),
        ('[]', True),
        ('{[(){}]}', True),
        ('', True), #technically this is balanced
        ('[[[', False),
        (']]]', False),
        ('][', False),
    )
    for test_case in test_cases:
        print('checking "{}"'.format(test_case))
        assert check_valid(test_case[0]) == test_case[1]
