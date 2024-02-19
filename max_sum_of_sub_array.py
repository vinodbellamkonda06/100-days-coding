def max_sum_of_sub_arrays(array,size):
    sub_array = []
    for i in range(len(array)):
        sub_array.append(array[i:i + size])
        
    return max([array for array in sub_array if len(array) == size])
     
print(max_sum_of_sub_arrays([2, 3, 4, 5, 6, 7],3))