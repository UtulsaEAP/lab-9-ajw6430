def int_to_reverse_binary(num1):
    x = num1
    sepRevBin = []
    if num1 == 0:
        binary_val = '0'
    else:
        while x >= 1:
            digit = x%2
            sepRevBin.append(str(digit))
            x = x//2
        binary_val = ''.join(sepRevBin)
    return binary_val;


def string_reverse(input_string): 
    reverse_input = input_string[::-1]
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)