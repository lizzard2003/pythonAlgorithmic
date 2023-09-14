# Write a python function to find the second largest number in 
#a list of interger 
#not sorted

def find_second_largest(numbers):
    if len(numbers) < 2: # the  list has to have at least 2 numbers to compare
        return "List must contain at least two numbers"
    
    largest = second_largest = float('-inf')  # Initialize both variables to negative infinity

    for num in numbers: # going through the list of numbers
        if num > largest: # checks to see if the current number is greater than the current largest
            second_largest = largest # the largest is assigned the second largest because we found a larger num
            largest = num # the current num now becomes the largest 
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no second largest element"
    
    return second_largest


numbers = [10, 5, 20, 2, 8]
result = find_second_largest(numbers)
print("The second largest number is:", result)
