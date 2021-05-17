n = input()
half = len(n) // 2

first_half = n[:half]
second_half = n[half:]
first_half = list(map(int, first_half))
second_half = list(map(int, second_half))

if sum(first_half) == sum(second_half):
    print("LUCKY")
else:
    print("READY")