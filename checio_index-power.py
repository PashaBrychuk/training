def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n <= len(array)-1:
        z = array[n]
        return z**n
    return -1
print index_power([1, 2, 3, 4], 2)
print index_power([1, 3, 10, 100], 3)