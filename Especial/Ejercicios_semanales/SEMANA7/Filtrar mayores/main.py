import matrix_functions

numbers = [
    [3, 5, 4, 3],
    [6, 7, 5, 8, 9],
    [2, 1, 5],
    [2, 3, 1],
    [8, 3, 2, 4]
]
threshold = 4
result = matrix_functions.pass_highers(numbers, threshold)
print(result)
