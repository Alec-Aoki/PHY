import random
import os

def generate_knapsack_testcase(max_items):
    # Generate bag weight (between max_items and 3 * max_items)
    bag_weight = random.randint(max_items, 3 * max_items)
    
    # Generate items (weight between 1 and bag_weight/2, value between 1 and 100)
    items = [(random.randint(1, 100), random.randint(1, bag_weight // 2)) for _ in range(max_items)]
    
    return bag_weight, items

def solve_knapsack(bag_weight, items):
    n = len(items)
    dp = [[0 for _ in range(bag_weight + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, bag_weight + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(items[i-1][0] + dp[i-1][w-items[i-1][1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][bag_weight]

def write_testcase_to_file(filename, max_items, bag_weight, items):
    with open(filename, 'w') as f:
        f.write(f"{max_items} {bag_weight}\n")
        for value, weight in items:
            f.write(f"{value} {weight}\n")

def main():
    max_items = int(input("Enter the maximum number of items: "))
    bag_weight, items = generate_knapsack_testcase(max_items)
    
    # Solve the knapsack problem
    optimal_value = solve_knapsack(bag_weight, items)
    print(f"Optimal value: {optimal_value}")
    
    # Write test case to file
    filename = "knapsack_testcase.in"
    write_testcase_to_file(filename, max_items, bag_weight, items)
    print(f"Test case written to {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()