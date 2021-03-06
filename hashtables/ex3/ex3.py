def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    dct = {}
    result = []

    # Looping thru the lists

    for inner_array in arrays:

        for item in inner_array:

            if item not in dct:

                dct[item] = 0
            
            # Counting each appearance

            dct[item] += 1

    # if the counting match the number of inner arrays, it means
    # this number is in all arrays.

    for key,value in dct.items():

        if value == len(arrays):

            result.append(key)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
