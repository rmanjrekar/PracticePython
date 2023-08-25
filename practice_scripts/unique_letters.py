'''
Write a function (you can name it whatever you want) that takes any word as a parameter, and returns all of its unique letters (without repetition) in alphabetical order.
For example, if when calling this function we pass the word "entertaining", it should return ['a', 'e', 'g', 'i', 'n', 'r', 't']
'''

def unrepeated_letters(word):

    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list

if __name__ == "__main__":
    print(unrepeated_letters('entertaining'))        # ['a', 'e', 'g', 'i', 'n', 'r', 't']
    print(unrepeated_letters('pineapple'))           # ['a', 'e', 'i', 'l', 'n', 'p']
