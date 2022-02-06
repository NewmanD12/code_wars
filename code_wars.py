def likes(names):
    """
    takes a list of names and depending on length, returns who like it
    """
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

###############################################################

def square_sum(numbers):
    """
    takes list of numbers and returns a sum of the numbers squared
    """
    squared_Sum = sum([x**2 for x in numbers])
    return squared_Sum

square_sum([1, 2])

###############################################################

def create_phone_number(n):
    strings = [str(x) for x in n]
    area_code = ''.join(strings[:3])
    exchange_code = ''.join(strings[3:6])
    line_number = ''.join(strings[6:])
    res = '(' + area_code + ')' + ' ' + exchange_code + '-' + line_number
    return res

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

###############################################################

def high(str):
    '''
    takes a string of words and parses each word
    assigns value for each letter
    returns the word with the highest score
    '''
    word_and_score_dict = {}
    str = str.split(' ')
    for i in str:
        if i not in word_and_score_dict:
            score = 0
            for j in i:
                print(ord(j) - 96, j)
                score += ord(j) - 96
            word_and_score_dict[i] = score
    # print(word_and_score_dict)
    maxCount = 0
    most_valuable_word = [] 
    for k,v in word_and_score_dict.items():
        print(k,v)
        if v > maxCount:
            maxCount = v
            most_valuable_word.clear()
            most_valuable_word.append(k)
    return most_valuable_word[0]


# high('man i need a taxi up to ubud')
high('what time are we climbing up the volcano')
