"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # Print each item in the given list
    # >>> output_all_items(1, "hello", True)
    # >>> 1
    # >>> hello
    # >>> True

    for item in items:
        print(item)


def get_all_evens(nums):
    # Given a list of numbers, return a list of all even numbers
    # get_all_evens([7,8,10,1,2,2])
    # [8,10,2,2]
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


print(get_all_evens([7, 8, 10, 1, 2, 2]))


def get_odd_indices(items):
    # Given a list, return all elements at odd numbered indices
    # >>> get_odd_indices([1, "hello", True, 500])
    # ["hello", 500]

    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])

    return result


print(get_odd_indices([1, "hello", True, 500]))


def print_as_numbered_list(items):
    # Given a list, output a numbered list
    # print_as_numbered_list([1, "hello", True])
    # 1. 1
    # 2. hello
    # 3. True

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    # Return a list of numbers in a certain range
    # get_range(0,5)
    # [0, 1, 2, 3, 4]

    nums = []

    for num in range(start, stop):
        nums.append(num)
    return nums


def censor_vowels(word):
    # Given a string, return a string where vowels are replaced with "*"
    # censor_vowels("hello")
    # "h*ll*"

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    # Given a string in snake case, return a string in upper camel case

    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)


def longest_word_length(words):
    # Return the length of the longest word in the given arrya of words

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
