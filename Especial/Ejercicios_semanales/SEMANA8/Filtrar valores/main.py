import number_functions

numbers = {
    'a': 1, 'b': 4, 'c': 7, 'd': 8, 'e': 3,
    'f': 10, 'g': 12, 'h': 13, 'i': 14, 'j': 15
}
start = 4
end = 10
filtered_numbers = number_functions.filter_values(numbers, start, end)
print(filtered_numbers)
