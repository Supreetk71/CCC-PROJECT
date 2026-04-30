# Smart Diet Planner (Greedy + Dynamic Programming)

foods = [
    {"name": "Rice", "cost": 40, "calories": 200},
    {"name": "Chicken", "cost": 120, "calories": 250},
    {"name": "Egg", "cost": 10, "calories": 70},
    {"name": "Milk", "cost": 30, "calories": 100},
    {"name": "Apple", "cost": 50, "calories": 80},
    {"name": "Bread", "cost": 25, "calories": 150}
]

# ---------------- GREEDY ----------------
def greedy_diet(budget):
    foods_sorted = sorted(foods, key=lambda x: x["calories"]/x["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected = []

    for food in foods_sorted:
        if total_cost + food["cost"] <= budget:
            selected.append(food["name"])
            total_cost += food["cost"]
            total_calories += food["calories"]

    return selected, total_cost, total_calories


# ---------------- DP (Knapsack) ----------------
def dp_diet(budget):
    n = len(foods)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if foods[i-1]["cost"] <= w:
                dp[i][w] = max(
                    foods[i-1]["calories"] + dp[i-1][w - foods[i-1]["cost"]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # Backtracking
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(foods[i-1]["name"])
            w -= foods[i-1]["cost"]

    return selected, dp[n][budget]


# ---------------- MAIN ----------------
budget = int(input("Enter your budget: "))

g_sel, g_cost, g_cal = greedy_diet(budget)
dp_sel, dp_cal = dp_diet(budget)

print("\n--- Greedy Result ---")
print("Foods:", g_sel)
print("Cost:", g_cost, "Calories:", g_cal)

print("\n--- DP Result ---")
print("Foods:", dp_sel)
print("Calories:", dp_cal)
