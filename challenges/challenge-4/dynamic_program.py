# coding: utf-8
#!python
# dynamic_program.py
# By Timofey Makhlay (github.com/timomak/cs-2.2/challenges/challenge-4)

def largestSubset(array, n):
    """
    Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element.
    Resources: https://www.geeksforgeeks.org/largest-divisible-pairs-subset/
    Running:
    """

    array.sort()  # O(n * log(n))

    largest_divisible = [0 for i in range(n)] # Storing largest divisible subset.

    largest_divisible[n - 1] = 1 # Last element is set to largest

    # Fill values for smaller elements
    for i in range(n - 2, -1, -1):

        # Find all multiples of array[i]
        # and consider the multiple
        # that has largest subset
        # beginning with it.
        maximum = 0
        for j in range(i + 1, n):
            if array[j] % array[i] == 0:
                maximum = max(maximum, largest_divisible[j])
        largest_divisible[i] = 1 + maximum

    # Return maximum value from largest_divisible list
    return max(largest_divisible)

# Driver Code
a = [ 1, 3, 6, 13, 17, 18 ]
n = len(a)
print("The optimal solution is: ",largestSubset(a, n))
