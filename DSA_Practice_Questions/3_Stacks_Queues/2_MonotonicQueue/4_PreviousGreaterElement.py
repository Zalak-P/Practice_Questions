# Problem: https://www.geeksforgeeks.org/dsa/previous-greater-element/
# Core Trick: Pop elements until greatest element discovered. 

def find_previous_greater(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # If stack is not empty, the top is the previous greater element
        if stack:
            result[i] = stack[-1]
        # Push current element to stack for future comparisons
        stack.append(arr[i])
        
    return result

def find_previous_smaller(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        # If stack is not empty, the top is the previous greater element
        if stack:
            result[i] = stack[-1]
        # Push current element to stack for future comparisons
        stack.append(arr[i])
        
    return result