# coding: utf-8
#!python
# challenge-4.py
# By Timofey Makhlay (github.com/timomak/cs-2.2/challenges/challenge-4)

def knapsack(Capacity, items, n):
    """Given the maximum capacity and items list, pick the highest value items with the best use of the capacity"""

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
    pass

# To test above function
items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
Capacity = 50
n = len(items)
print(knapsack(Capacity, items, n))
