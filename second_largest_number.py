def second_large_number(array):
    for i in range(len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array[-2]

second_large_number(array)



def second_largest_number(array):
    first = second = 0
    for num in array:
        if num > first:
            second = first
            first = num
    return second

second_largest_number([10, 20, 3, 1, 5, 8, 25])