from functools import reduce

# question 9
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

print(factorial(5))

# question 10
concatenate_strings = lambda strings: reduce(lambda x, y: x + " " + y, strings)

strings = ["Hello", "world", "today", "is", "a", "great", "day"]
print(concatenate_strings(strings))

# question 11
def cumulative_sum_of_squares(numbers_lists):
    evens = map(lambda numbers: filter(lambda n: n % 2 == 0, numbers), numbers_lists)
    sum_squares = map(lambda evens: reduce(lambda x,y: x + y, map(lambda even: even ** 2, evens)), evens)
    # sum_squares is based on value of evens, so nested lambda count is 3 + 2 = 5
    # total nested lambda count in function is 3 + 2 + 1 = 6
    return reduce(lambda x, y: x + y, sum_squares)

input = [[1,2,3], [4,5,6], [7,8,9]]
print(cumulative_sum_of_squares(input))

# question 12
nums = [1,2,3,4,5,6]
sum_squared = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)), 0)
print(sum_squared)

# question 13
count_palindromes = lambda strings_lists: list(map(lambda strings: len(list(filter(lambda s: s == s[::-1], strings))), strings_lists))
input = [["aba", "abc", "aba"], ["def", "ghi", "jkl", "asdfghjkjhgfdsa"]]
print(count_palindromes(input))