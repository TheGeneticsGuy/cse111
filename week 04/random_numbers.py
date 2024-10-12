# TEAM:         Group 19 (Wed 8pm MT)
# ACTIVITY:     Lists (Week 04)
# DATE:         2024-10-09


import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words_list = ['join', 'love', 'smile']

    print(numbers)

    append_random_numbers(numbers,1,5,15)
    print(numbers)

    append_random_numbers(numbers,3,5,15)
    print(numbers)

    append_random_words(words_list , 1)
    print(words_list)

    append_random_words(words_list , 3)
    print(words_list)

def append_random_numbers(numbers_list , quantity=1 , lower_range=0, upper_range=500):
    '''
        Append random numbers onto A numbers list that are between 0 and 500
        Parameters
            numbers_list: A list of numbers to append to
            quantity: how many random numbers to append
        Return: nothing. It's unnecessary for this function to return
            anything because this function changes the numbers_list. Memory Reference of listy is past, not a new list. The
    '''
    print()

    for num in range(quantity):
        random_number = round ( random.uniform ( lower_range , upper_range ) , 1 )
        numbers_list.append(random_number)

def append_random_words(words_list , quantity=1):

    words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellowfruit",
    "zucchini", "apricot", "blackberry", "cantaloupe", "dragonfruit", "gooseberry", "jackfruit"
    ]

    for num in range(quantity):
        random_word_index = random.randint ( 0 , len(words) - 1 )
        words_list.append( words[random_word_index] )


# If file is imported, it will skip this main call
if __name__ == "__main__":
    print()
    main()
    print()
