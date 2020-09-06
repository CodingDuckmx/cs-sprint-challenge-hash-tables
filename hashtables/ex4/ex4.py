def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # built a dictionary of all positive numbers
    dct = {i:None for i in a if i > 0}

    result = []

    # Verify if for each negative number in the list, there's its negative.

    for i in a:

        if i < 0:

            if -i in dct:

                # if matching, append it.

                result.append(-i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
