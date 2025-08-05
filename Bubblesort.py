# List of favorite foods
foods = ["Biryani", "Pizza", "Burger", "Dosa", "Sushi", "Noodles"]
# Bubble Sort to sort foods by length of name
n = len(foods)
for i in range(n):
    for j in range(0, n - i - 1):
        # Compare lengths of adjacent food names
        if len(foods[j]) > len(foods[j + 1]):
            # Swap if needed
            foods[j], foods[j + 1] = foods[j + 1], foods[j]
# Print sorted list
print("Favorite foods sorted by length:")
print(foods)
