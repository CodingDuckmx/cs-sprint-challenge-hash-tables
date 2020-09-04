def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    dct = {item : None for item in arrays[0]}
    removable_keys  = []
    result = []

    for inner_list in arrays[1:]:

        for key in dct.keys():

            if key not in inner_list:

                removable_keys.append(key)

    for key in removable_keys:

        try:

            dct.pop(key)

        except:

            continue        

    print(dct)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
