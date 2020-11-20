def find_buy_sell_stock_price(arr):
    current_buy = arr[0]
    global_sell = arr[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(arr)):
        current_profit = arr[i] - current_buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = arr[i]

        if current_buy > arr[i]:
            current_buy = arr[i]
    return global_sell - global_profit, global_sell



array = [1, 2, 3, 4, 3, 2, 1, 2, 5]
result = find_buy_sell_stock_price(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))