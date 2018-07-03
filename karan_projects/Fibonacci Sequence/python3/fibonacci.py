import sys

def matrix_mul(first_matrix, second_matrix):
    return [
        [first_matrix[0][0]*second_matrix[0][0] + first_matrix[0][1]*second_matrix[1][0],
        first_matrix[0][0]*second_matrix[0][1] + first_matrix[0][1]*second_matrix[1][1]],
        [first_matrix[1][0]*second_matrix[0][0] + first_matrix[1][1]*second_matrix[1][0],
        first_matrix[1][0]*second_matrix[0][1] + first_matrix[1][1]*second_matrix[1][1]]
    ]

def matrix_power(matrix, power):
    assert(len(matrix) == 2)
    assert(len(matrix[0]) == 2)
    assert(len(matrix[1]) == 2)
    if power == 0:
        return [[1, 0], [0, 1]]
    if power % 2 == 0:
        temp = matrix_power(matrix, power // 2)
        return matrix_mul(temp, temp)
    else:
        temp = matrix_power(matrix, power - 1)
        return matrix_mul(temp, matrix)

def fibonacci(n):
    a = [[1, 1], [1, 0]]
    a = matrix_power(a, n)
    return a[0][0]

if len(sys.argv) != 2:
    print(
        'No number detected\n' +
        'You have to run it in the following way\n' + 
        'python3 ' + sys.argv[0] + ' [int]\n' + 
        'where [int] is index of Fibonacci number you want to get'
        )
    print(
        'You have to type positive int as the second argument' +
        'The program will print nth Fibonacci number' +
        'Fibonacci number is defined as the following' +
        'F_0 = 1, F_1 = 1, F_{n+2} = F_{n+1} + F_{n} for n>=0'
        )
else:
    try:
        print(fibonacci(int(sys.argv[1])))
    except:
        print(
            'You have to type positive int as the second argument\n' +
            'The program will print nth Fibonacci number\n' +
            'Fibonacci number is defined as the following\n' +
            'F_0 = 1, F_1 = 1, F_{n+2} = F_{n+1} + F_{n} for n>=0'
            )

