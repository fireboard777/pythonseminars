def powers_of_two(N):
    power = 0
    result = []

    while 2 ** power <= N:
        result.append(2 ** power)
        power += 1

    return result

# Пример использования:
N = 100
powers = powers_of_two(N)

print("Целые степени двойки, не превосходящие", N, ":")
for power in powers:
    print(power)
