# Taken From
# Iterating Over Data
# Problem-Set While Loops #11


def silly_sum():
    input_int = input("Enter a number: ")
    """Reads numbers from the user (using input_int),
    summing until the user enters 0 or the sum reaches/exceeds 1000.
    """
    total = 0
    while total < 1000:
        num = input_int("Enter a number (0 to stop): ")
        if num == 0:
            break
        total += num
    print("Final sum:", total)
    return total

