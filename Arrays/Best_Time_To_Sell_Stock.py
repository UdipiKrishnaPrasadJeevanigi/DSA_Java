prices = [7,1,5,3,6,4]

min_price = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    profit = prices[i]-min_price
    if(profit > max_profit):
        max_profit = profit
    if(prices[i] < min_price):
        min_price = prices[i]
print(max_profit)
    