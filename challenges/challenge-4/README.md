# Largest Subset Dynamic Programming

Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element.

References:
* Tim and his repo ([link](https://github.com/daisukiyo/cs-2.2/blob/master/challenges/challenge-4/Part-1/README.md)).
* Geeksforgeeks ([link](https://www.geeksforgeeks.org/largest-divisible-pairs-subset/))

## Largest Subset
> Code
```Python
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
```
> Input
```
a = [ 1, 3, 6, 13, 17, 18 ]
n = len(a)
```

> Output
```
The optimal solution is: 4
```

## Steps Taken for Dynamic Programming (Thanks to Tim for layout and info here.)
1. **Identify the subproblems**</br>
First we check if the last item in the list is divisible. If it is, we pair it with every other item and repeat the process until we have all the divisible values matched against each other.
1. **What does the solution roughly look like**</br>
The solution should be the highest divisible value by another item in the list.
1. **Define a base case**</br>
The base case is if there are no items return 0 for our value.
1. **Compute the value of an optimal solution (recurse and memoize)**</br>
```
# Find all multiples of array[i]
# and consider the multiple
# that has largest subset
# beginning with it.

if array[j] % array[i] == 0:
    maximum = max(maximum, largest_divisible[j])
```
5. **Solve original problem - reconstruct from the sub-problems**
