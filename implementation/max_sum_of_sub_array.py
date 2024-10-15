def max_sum_of_sub_arrays(array,size):
    """

    :param array:  List of integers
    :param size:  int
    :return: sub array List of integers
    """
    sub_array = []
    for i in range(len(array)):
        sub_array.append(array[i:i + size])
        
    return max([array for array in sub_array if len(array) == size])

