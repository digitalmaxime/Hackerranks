import copy


if __name__ == '__main__':
    coins_count = 2

    coins = [0, 5, 4]

    amount = 11
    
    coins = sorted(coins)
    if 0 in coins:
        coins.remove(0)
        
    temp_total = 0
    failed_first_input = set()
    temp_amount = copy.copy(amount)
    while temp_amount != 0:
        temp_amount = copy.copy(amount)
        temp_total = 0
        for index, coin in reversed(list(enumerate(coins))):
            # if coin in failed_first_input:
            #     continue
            
            if coin <= temp_amount :
                nbCoinInAmount = temp_amount // coin
                temp_amount -= coin * nbCoinInAmount
                temp_total += nbCoinInAmount
                # print("-- ", coin, " * ", nbCoinInAmount)
                if temp_total == 0:
                    break

        if temp_amount != 0:
            coins.pop()
            # failed_first_input.add(coins[0])
            
        if len(coins) == 0:
            temp_total = -1
            break
    
    print(temp_total)