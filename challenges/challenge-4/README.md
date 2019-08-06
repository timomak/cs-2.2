# Knap Sack Dynamic Programming

Given the maximum capacity and items list, pick the highest value items with the best use of the capacity.

References:
* Tim and his repo ([link](https://github.com/daisukiyo/cs-2.2/blob/master/challenges/challenge-4/Part-1/README.md)).
* Geeksforgeeks ([link](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/))

## Original Knap Sack
> Original
```Python
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
```
> Input
```
items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
Capacity = 50
n = len(items)
```

> Output
```
230
```

## Dynamic Programming Knapsack
> Original
```Python
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

    return K[n][Capacity][0]
```
> Input
```
items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
Capacity = 50
n = len(items)
```

> Output
```
The value of the optimal solution to the knapsack problem is V=230
```

## Steps Taken for Dynamic Programming (Thanks to Tim for layout and info here.)
1. Identify the subproblems
First we check if the last item in the list exceeds the capacity. If it doesn't we pair it with every other item and repeat the process until the combined capacity of the items approaches or meets our maximum capacity size.
1. What does the solution roughly look like
The solution should return the highest value of items we can fit in our Knap Sack based on Capacity and out list of items.
1. Define a base case
The base case is if there are no items or the capacity is 0, return 0 for our value
1. Compute the value of an optimal solution (recurse and memoize)
```
# Returns the maximum of two cases:
# (1) nth item included
# (2) not included
```
`return max(value[n-1] + knapSack(Capacity-weight[n-1], items, n-1) # Add it to the bag`
`return knapSack(Capacity, items, n-1)) # or don't add it to the bag`
1. Solve original problem - reconstruct from the sub-problems
