def fibonacci(n):
    a = 0
    b = 1
    c = a
    if n < 0:
        c = -1
    elif n == 0:
        c = a
    elif n == 1:
        c = b
    else:    
        for x in range((n-1)):
            c = a + b
            a = b
            b = c
    return c

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')