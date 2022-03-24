"""List comprehension exercises"""
import math

def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [
        name 
        for name in names 
        if name[0].upper() in "AEIOU"
        ]


def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [x**i 
            for i, x in enumerate(numbers)
            ]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [
        number 
        for lists in matrix 
        for number in lists
        ] 


def reverse_difference(x):
    """Return list subtracted from the reverse of itself."""
    return[
        x[i] - x[-i-1]
        for i in range(len(x))
    ]

def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [num1 + num2 for num1, num2, in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]


def transpose(matrix):
    """Return a transposed version of given list of lists."""
    if matrix:
        return [  
            [matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))
        ]
    else:
        return []

def get_factors(number):
    """Return a list of all factors of the given number."""
    return [n for n in range(1, number+1)  if number%n == 0]

def triples(N):
    """Return list of Pythagorean triples less than input num."""
    
    return [
        (i, j, int(math.sqrt(i**2 + j**2)))
        for i in range(1,N)
        for j in range(i,N)
        if math.sqrt(i**2 + j**2)%1 == 0 and math.sqrt(i**2 + j**2) < N
    ]
