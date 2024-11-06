def fractionalKnap(items, capacity):
    profit = 0.0
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    for item in items:
        if capacity > item[1]:
            profit += item[0]
            capacity -= item[1]
        else:
            profit += capacity * item[0] / item[1]
            break
    
    print("Maximum Profit:", profit)

# Taking input from user
num_items = int(input("Enter the number of items: "))
items = []

for i in range(num_items):
    profit = float(input(f"Enter profit for item {i+1}: "))
    weight = float(input(f"Enter weight for item {i+1}: "))
    items.append((profit, weight))

capacity = float(input("Enter the capacity of the knapsack: "))

# Call the function with user-provided inputs
fractionalKnap(items, capacity)
