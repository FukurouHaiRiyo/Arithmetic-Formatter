def arithmetic_arranger(lista, display = False):    
    arr = ''

    if len(lista) > 5:
        arr = 'Too many problems'
        return arr

    ops = list(map(lambda x: x.split()[1], lista))

    if set(ops) != {'+', '-'} and len(set(ops))!=2:
        arr = 'There must be only \'+\' and \'-\' as operations'
        return arr

    nums = [] 

    for i in lista:
        p = i.split()
        nums.extend([p[0], p[2]])
    
    if not all(map(lambda x: x.isdigit(), nums)):
        arr = 'Numbers must contain digits only'
        return arr

    if not all(map(lambda x: x.__len__() < 5, nums)):
        arr = 'Numbers can\'t be longer than 4 digits'
        return arr

    top = ''
    lines = ''
    vals = list(map(lambda x: eval(x), lista))
    solution = ''

    for i in range(0, len(nums), 2):
        space = max(len(nums[i]), len(nums[i + 1])) + 2
        top += nums[i].rjust(space)
        lines += '-' * space
        solution += str(vals[i // 2]).rjust(space)

        if i != len(nums) - 2:
            top += ' ' * 4
            lines += ' ' * 4
            solution += ' ' * 4
    
    
    bottom = ' '

    for i in range(1, len(nums), 2):
        space = max(len(nums[i-1]), len(nums[i])) + 1
        bottom += ops[i // 2]
        bottom += nums[i].rjust(space)

        if i != len(nums) - 1:
            bottom += ' ' * 4
    
    if display:
        arr = '\n'.join((top, bottom, lines, solution))
    else:
        arr = '\n'.join((top, bottom, lines))
    
    return arr


if __name__ == '__main__':
    lista = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(lista))
