import csv
from collections import Counter
import random

expenses = []

# Prompt the user to set a monthly budget
monthly_budget = float(input("Enter your monthly budget: $"))

# -------------------------------
# Load saved expenses from CSV file
def load_expenses_from_file():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                })
        print("Previous expenses loaded successfully.")
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")

# Save current expenses to CSV file
def save_expenses_to_file():
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

# -------------------------------
# Add new expense
def add_expense():
    date = input("Enter date (year-month-day, e.g.2020-06-14): ")
    category = input("Enter category (e.g. Food, Transport, Bills): ")
    try:
        amount = float(input("Enter amount: $"))
        expenses.append({"date": date, "category": category, "amount": amount})
        save_expenses_to_file()
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

# -------------------------------
# View summary of total and remaining budget
def view_summary():
    total_spent = sum(exp["amount"] for exp in expenses)
    print("\n======= Budget Summary =======")
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Remaining budget: ${monthly_budget - total_spent:.2f}")
    if total_spent > monthly_budget:
        suggest_savings_tip()

# -------------------------------
# Show Top 3 Categories
def show_top_3_categories():
    if not expenses:
        print("No expenses recorded yet.")
        return
    category_totals = {}
    for exp in expenses:
        category = exp["category"]
        category_totals[category] = category_totals.get(category, 0) + exp["amount"]

    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    print("\nTop 3 Expense Categories:")
    for i, (cat, total) in enumerate(sorted_categories[:3], start=1):
        print(f"{i}. {cat} - ${total:.2f}")

# -------------------------------
# Suggest a random savings tip
def suggest_savings_tip():
    saving_tips = [
        "Try cooking at home instead of eating out.",
        "Limit non-essential purchases this week.",
        "Consider switching to a lower-cost mobile plan.",
        "Cut back on subscription services you don't use.",
        "Plan a staycation instead of a vacation.",
        "Use a grocery list to avoid impulse buys.",
        "Turn off unused lights and electronics to save energy."
    ]
    print("\n⚠️ Overspending Alert!")
    print("Tip:", random.choice(saving_tips))

# -------------------------------
# Main Program Menu
def main():
    load_expenses_from_file()
    while True:
        print("\n====== SMART BUDGET BUDDY ======")
        print("1. Add Expense")
        print("2. View Budget Summary")
        print("3. View Top 3 Categories")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            show_top_3_categories()
        elif choice == "4":
            print("Goodbye! Your expenses are saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
