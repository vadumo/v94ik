def count_positives_sum_negatives(arr):
    '''
Given an array of integers.
Return an array, where the first element is the count of positives
numbers and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array.'''
    if not arr: 
        return []
    a = 0
    b = 0
    for i in arr:
        if i > 0:
            a += 1
        elif i < 0:
            b += i
    return [a, b]