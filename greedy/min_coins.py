class MinCoins:
    @classmethod
    def min_coins(cls, coins, amount):
        coins = sorted(coins, reverse=True)
        res = 0
        for counter in range(len(coins)):
            if coins[counter] <= amount:
                c = amount // coins[counter]
                res += c
                amount -= c*coins[counter]

            if amount == 0:
                break

        return res


if __name__ == "__main__":
    obj = MinCoins()
    coins = [5, 10, 1, 2]
    amount = 52
    print(obj.min_coins(coins, amount))
