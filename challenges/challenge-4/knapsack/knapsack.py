# coding: utf-8
#!python
# knapsack.py
# By Timofey Makhlay (github.com/timomak/cs-2.2/challenges/challenge-4)

def knapsack(Capacity, items, n):
    """
    Given the maximum capacity and items list, pick the highest value items with the best use of the capacity.
    Resources: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    Runtime: (2^n)
    """

    # Base Case
    if n == 0 or Capacity == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (items[n-1][1] > Capacity): # items[ ( "item name", weight, value ), ...]
        print("Item weight is more than capacity")
        return knapsack(Capacity, items, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(items[n-1][2] + knapsack(Capacity - items[n-1][1] , items, n-1),
                   knapsack(Capacity, items, n-1))

def knapsack_dp(Capacity, items, n):
    """
    Given the maximum capacity and items list, pick the highest value items with the best use of the capacity. Using Dynamic programming.
    Resources: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    Runtime: (2^n)
    """
    K = [[[0] for x in range(Capacity + 1)] for y in range(n + 1)] # [[0, ...range(Capacity + 1)], ...range(n + 1)]
    # return K


    # Build table K[][] in bottom up manner
    for y in range(n+1):
        for w in range(Capacity+1):
            if y == 0 or w == 0:
                K[y][w][0] = 0
            elif items[y - 1][1] <= w:
                K[y][w][0] = max(items[y - 1][2] + K[y - 1][w - items[y-1][1]][0],  K[y-1][w][0])
                K[y][w].append(items[y - 1][0])
            else:
                K[y][w][0] = K[y - 1][w][0]
                K[y][w].append(items[y - 1][0])

    return_value = K[n][Capacity]

    return K[n][Capacity][0]

# To test above function
items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
Capacity = 50
n = len(items)
# newlist = items[1:]
# print(newlist)
print("The value of the optimal solution to the knapsack problem is V={}".format(knapsack_dp(Capacity, items, n)))
