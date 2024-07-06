def mbs(in_str):
    '''
    Have the function  MultipleBrackets(str) take the str parameter being passed and return 1 #ofBrackets
    if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example:
    if str is "(hello [world])(!)", then the output should be 1 3 because all the brackets are matched and
    there are 3 pairs of brackets, but if str is "((hello [world])" the the output should be 0 because the
    brackets do not correctly match up. Only "(", ")", "[", and "]" will be used as brackets. If str contains
    no brackets return 1.
    console.log('Sample test passing: ' + (MultipleBrackets("h[ello](!)") == '1 2'));
    console.log('Sample test passing: ' + (MultipleBrackets("one(bracket)") == '1 1'));
    '''
    stack, count = [], 0
    for char in in_str:
        if char in set("()[]"):
            if char in set(')]'):
                if not stack:
                    return 0
                if (
                    (stack[-1] == '(' and char != ')') or
                    (stack[-1] == '[' and char != ']')
                ):
                    return 0
                else:
                    stack.pop()
                    count +=1
            else:
                stack.append(char)
    if not stack:
        return (1, count)
    return  0



if __name__ == '__main__':
    test_cases = (
        ('h[ello](!)', (1,2,)),
        ('one(bracket)',(1,1,)),
        ('', (1,0,)), #technically this is balanced
        ('foo([]', 0),
        (']]]', 0),
        ('][', 0),
    )
    for case, result in test_cases:
        print(f'checking "{case}"')
        assert mbs(case) == result
