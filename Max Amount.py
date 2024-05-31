"""
Purpose
The purpose of this algorithm can be summarized as follows:

Maximizing the Sum:
The core objective is to maximize the sum of the quantities picked over m operations.
By repeatedly picking the largest available quantity and then decrementing it, the function ensures that the 
highest possible values are being added to the total sum, thus maximizing the final result.

Example Walkthrough


Initial State:

quantity = [3, 1, 4, 1, 5]
m = 3
Iteration 1:

Sort quantity: [1, 1, 3, 4, 5]
Add the largest element to maximumAmount: maximumAmount += 5 -> maximumAmount = 5
Decrease the largest element by 1: quantity = [1, 1, 3, 4, 4]
Iteration 2:

Sort quantity: [1, 1, 3, 4, 4]
Add the largest element to maximumAmount: maximumAmount += 4 -> maximumAmount = 9
Decrease the largest element by 1: quantity = [1, 1, 3, 4, 3]
Iteration 3:

Sort quantity: [1, 1, 3, 3, 4]
Add the largest element to maximumAmount: maximumAmount += 4 -> maximumAmount = 13
Decrease the largest element by 1: quantity = [1, 1, 3, 3, 3]
Final Output:

maximumAmount = 13

The code's purpose is to ensure that the sum of the selected quantities is as large 
as possible by always selecting the highest available quantity and then reducing it for subsequent selections. 
This greedy approach works effectively to maximize the total sum given the constraints.
"""

def getMaximumAmount(qty, m):
    max_amount = 0
    n = len(qty)

    for i in range(m):
        qty.sort()
        max_amount = max_amount + qty[n-1]

        qty[n-1] -= 1
        print(qty)
    return max_amount

print(getMaximumAmount([3, 1, 4, 1, 5], 3))