def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    if len(weights) > 1: 

        # This is a dictionary with the possible indexes of the weights list.
        # In each slot, we have a list of the result of summing the ith index (the key if the dictionary) and
        # the jth entry of the weights list.

        dct = { weights[i]+ weights[j]  : (j,i)   for i in range(length) for j in range(i+1,length)}

        if limit in dct:

            return dct[limit]

    return None


if __name__ == "__main__":
    

    print(get_indices_of_item_weights([4, 6, 10, 15, 16],5,21))