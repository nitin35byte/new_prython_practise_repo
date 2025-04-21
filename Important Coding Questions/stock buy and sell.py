def max_profit(prices):

    n = len(prices)

    profit=0

    for i in range(1 , n):
        if prices[i] > prices[i-1]:
            profit+=prices[i] - prices[i-1]
    return profit

prices=[7 , 1 , 5 , 3 ,6 , 4]
print(max_profit(prices))