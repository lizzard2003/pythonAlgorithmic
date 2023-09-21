# find the smallest element in the array and exchange it with the element in the first position
# find the second smallest element and replace it in the second position

# find the minimum value
# create a variable called min_index and set it to the first position in the list (usually 0)
# iterate through the list and if a vulue is greater than the one at the
# min_index, update  min_index to the new position 

def find_min(xs):
    min_index= 0
    for i in range(len(xs)):
        if xs[i] <xs[min_index]:
            min_index = i
    return xs[min_index]

xs=[3,2, 5, 4, 10, 8, 12, 25]
min_value= find_min(xs)
print(f"The minimum value is {min_value} . ")

def selection_sort(xs):
    for i in range(len(xs)-1):
        min_index = i
        for j in range(i+1, len(xs)):
            if xs[j] <xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]

xs=[3,2, 5, 4, 1, 10, 8, 12, 25]
print(xs)
selection_sort(xs)
print(xs)
print(all(xs[i] <= xs[i +1] for i in range(len(xs)-1)))