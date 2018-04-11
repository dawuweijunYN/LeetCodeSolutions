candies = [0, 1, 2, 3, 3, 4]
candies_set = set(candies)
print(len(candies_set))
print(len(candies))
count = min(len(candies_set) + 1, (len(candies) + 1) // 2)
print(count)
