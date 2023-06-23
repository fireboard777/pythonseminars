def min_flips(coins):
    heads = sum(coins)  # количество монеток с решкой вверх
    tails = len(coins) - heads  # количество монеток с гербом вверх
    
    return min(heads, tails)

# Пример использования:
coins = [1, 0, 0, 1, 1]  # 1 обозначает решку, 0 обозначает герб
min_flips_needed = min_flips(coins)
print("Минимальное количество монеток, которые нужно перевернуть:", min_flips_needed)
