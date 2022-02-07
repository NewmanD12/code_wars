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

def anagrams(word, words):
    anagrams = []
    wordLetters = [x.lower() for x in word]
    wordLetters.sort()
    for i in words:
        split_word = [x.lower() for x in i]
        split_word.sort()
        if split_word == wordLetters:
            anagrams.append(i)
    return anagrams

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])


