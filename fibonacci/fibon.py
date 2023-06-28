def fibonacci(num):
    if num <= 0:
        return []
    # elif num == 1:
    #     return [0]
    # elif num == 2:
    #     return [0, 1]
    # elif num == 3:
    #     return [0, 1, 2]
    else:
        fibonacci_sequence = fibonacci(num - 1)
        fibonacci_sequence.append([-1] + fibonacci_sequence[-2])
        return fibonacci_sequence
