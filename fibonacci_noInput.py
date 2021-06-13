def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        n_2, n_1 = 0, 1
        #Calculate Fibonacci iteratively starting at the 3rd value up n (n+1 is used because ranges exclude the last value)
        for num in range(3, n+1):
            fib_term = n_2 + n_1
            n_2 = n_1
            n_1 = fib_term

        return fib_term



print(fibonacci(10))