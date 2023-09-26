# this uses the greedy algorith to make change the quickest
def make_change(target_amount):
    denominations=[100.00, 50.00, 20.00, 10.00, 5.00, 1.00] # you have to go from greatest to least
    coin_count = 0
    values=[]
    for coin in denominations:
        while target_amount >= coin: 
            target_amount -= coin # this is subtracting from original amount 
            values.append(coin)
            coin_count += 1
    return coin_count, values
print (make_change(22))
print (make_change(250))