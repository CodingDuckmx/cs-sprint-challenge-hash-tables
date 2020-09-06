# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Built a dictionary for the possible queries

    queries_dct = {query: [] for query in queries}
    result = []

    # Verify if each path could be inserted in the dictionary, comparing its tail to the dictionary key.

    for path in files:

        if path[path.rfind('/')+1:] in queries_dct:

            result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
