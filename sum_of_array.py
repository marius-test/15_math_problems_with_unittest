def sum_of_array(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result

if __name__ == '__main__':
    array1 = [1, 2, 3]
    print(sum_of_array(array1))
