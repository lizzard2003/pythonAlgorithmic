# this is brute force 
# it uses the a simple and insuficient approach  
def linear_search(data, target):
# enumerate function gives us both the value and index within a list

    for idx, val in enumerate(data):
        if val ==target:
            return idx
    return -1
data=[4, 5, 2, 7, 1, 8]
target = 2
result= linear_search(data, target)
if result== -1:
    print ("Item was not found")
else:
    print(f"Item found at position {result}. ")