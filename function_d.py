

def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    maximum_num = numbers[0]
    for num in numbers:
        if num > maximum_num:
            maximum_num = num
    return maximum_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))    
