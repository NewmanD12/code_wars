from functools import cache


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
                # print(ord(j) - 96, j)
                score += ord(j) - 96
            word_and_score_dict[i] = score
    # print(word_and_score_dict)
    maxCount = 0
    most_valuable_word = [] 
    for k,v in word_and_score_dict.items():
        # print(k,v)
        if v > maxCount:
            maxCount = v
            most_valuable_word.clear()
            most_valuable_word.append(k)
    return most_valuable_word[0]


# high('man i need a taxi up to ubud')
high('what time are we climbing up the volcano')

###############################################################

def expanded_form(num):
    num = str(num)
    segments = []
    for idx, val in enumerate(num):
        # print(idx, val)
        if int(val) > 0:
            # print(num[idx+1:])
            segment = val[0] + ('0' * len(num[idx+1:]))
            segments.append(segment)
    # print(' + '.join(segments))
    return ' + '.join(segments)


expanded_form(70304)

###############################################################

def find_uniq(arr):
    """
    takes an array of numbers, which are all the same execept ONE
    and returns the number that is unique
    """
    unique = None 
    for i in range(1, len(arr) -1):
        if arr[i] == arr[i + 1] and arr[i] != arr[i - 1]:
            unique = arr[i - 1] 
            break
        elif arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
            unique = arr[i]
            break
        elif arr[i] == arr[i - 1] and arr[i] != arr[i + 1]:
            unique = arr[i + 1]
            break
    return unique

find_uniq([ 1, 1, 1, 2, 1, 1 ])
find_uniq([ 2, 1, 1, 1, 1, 1 ])
find_uniq([ 1, 1, 1, 1, 1, 2 ])

###############################################################

def move_zeros(array):
    zeros = [x for x in array if x == 0]
    nums = [x for x in array if x != 0]
    return nums + zeros

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])

###############################################################


def duplicate_encode(word):
    word = word.lower()
    res = ''
    for i in word:
        if word.count(i) > 1:
            res += ')'
        else:
            res += '('
    return res

duplicate_encode("recede")

###############################################################

def sort_array(source_array):
    odds = [x for x in source_array if x % 2 == 1]
    evens = [x for x in source_array if x % 2 == 0]
    odds.sort()
    # print(odds + evens)
    return odds + evens


sort_array([5, 3, 2, 8, 1, 4])

###############################################################

def anagrams_1(word, words):
    anagrams = []
    wordLetters = [x.lower() for x in word]
    wordLetters.sort()
    for i in words:
        split_word = [x.lower() for x in i]
        split_word.sort()
        if split_word == wordLetters:
            anagrams.append(i)
    return anagrams

anagrams_1('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])

###############################################################

def increment_string(strng):
    res = ''
    if strng[-1].isnumeric():
        num = None
        word_len = 0
        zero_count = 0
        for idx, val in enumerate(strng):
            if val == 0:
                zero_count += 1
            if val.isnumeric():
                # print(val)
                num = int(strng[idx:])
                word_len = idx
                break
        res = strng[:word_len] + str(num + 1)
    else:
        res = strng + '1'
    # print(res)
    return res

increment_string("foobar099")
increment_string('foobar')

###############################################################

def scramble(s1, s2):
    word_1_dict = {}
    word_2_dict = {}
    res = True
    for i in s1:
        if i not in word_1_dict:
            word_1_dict[i] = 1
        else:
            word_1_dict[i] += 1
    
    for i in s2:
        if i not in word_2_dict:
            word_2_dict[i] = 1
        else:
            word_2_dict[i] += 1
    
    for k,v in word_2_dict.items():
        if k not in word_1_dict:
            res = False
        elif word_1_dict[k] < v:
            res = False
    return res
        


scramble('scriptjava', 'javascript')
scramble('katas', 'steak')

###############################################################

def cakes(recipe, available):
    '''
    this function takes a recipe (dictionary) and a dictinonary of
    available ingredients and returns how many of that recipe you could 
    make
    '''
    res = None
    if len(recipe) > len(available):
        return 0
    
    values = []
    for k,v in recipe.items():
        if k in available:
            values.append(int(str(available[k]/v).split('.')[0]))
    res = 0 if len(values) < len(recipe) else min(values)
    return res


recipe = {'chocolate': 37, 'cream': 10, 'cocoa': 6}
available = {'oil': 2371, 'crumbles': 3822, 'eggs': 672, 'sugar': 8924, 'apples': 1539, 
                'flour': 4607, 'cocoa': 9117, 'chocolate': 1336, 'nuts': 2483, 'pears': 9022}
cakes(recipe, available)

###############################################################

def duplicate_count(text):
    text = text.lower()
    char_and_count_dict = {}
    for i in text:
        if i in char_and_count_dict:
            char_and_count_dict[i] += 1
        else:    
            char_and_count_dict[i] = 1

    duplicate_count = 0
    for v in char_and_count_dict.values():
        if v > 1:
            duplicate_count += 1
    return duplicate_count

duplicate_count("abcdeaB")