def likes(names):
    res = ''
    if len(names) == 0:
        res = 'no one likes this'
    elif len(names) == 1:
        res = f'{names[0]} likes this'
    elif len(names) == 2:
        res = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        res = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        res = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    return res

likes([])
likes(['Peter'])
likes(['Peter', 'Alex'])
likes(['Peter', 'Alex', 'Mark'])
likes(['Peter', 'Alex', 'Mark', 'Max'])
