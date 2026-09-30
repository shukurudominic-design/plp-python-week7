# Create a list containing four fruits
fruits = ["avocado", "Banana", "Orange", "Apple"]

# Print the first and last fruits using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a fifth fruit
fruits.append("Pineapple")
print("After append:", fruits)

# Remove one fruit
fruits.remove("Orange")
print("After remove:", fruits)

# Print the number of fruits remaining
print("Number of fruits:", len(fruits))