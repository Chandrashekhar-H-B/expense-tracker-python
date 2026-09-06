#python
import csv
import os


# Name of the CSV file
file_name = "expenses.csv"


# Create the CSV file if it does not exist
def create_file():

    if not os.path.exists(file_name):

        file = open(file_name, "w", newline="")

        writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Description", "Amount"])

        file.close()


# Add a new expense
def add_expense():

    print("\n----- Add Expense -----")

    date = input("Enter date: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    file = open(file_name, "a", newline="")

    writer = csv.writer(file)

    writer.writerow([date, category, description, amount])

    file.close()

    print("Expense added successfully!")


# View all expenses
def view_expenses():

    print("\n----- All Expenses -----")

    file = open(file_name, "r")

    reader = csv.reader(file)

    # Skip the first row
    next(reader)

    found = False

    for row in reader:

        # Ignore empty rows
        if len(row) >= 4 and row[3] != "":

            found = True

            print("Date:", row[0])
            print("Category:", row[1])
            print("Description:", row[2])
            print("Amount: ₹", row[3])
            print("------------------------")

    file.close()

    if found == False:
        print("No expenses found.")


# Calculate total expenses
def show_total():

    total = 0

    file = open(file_name, "r")

    reader = csv.reader(file)

    # Skip the first row
    next(reader)

    for row in reader:

        # Check that the row contains an amount
        if len(row) >= 4 and row[3] != "":

            amount = float(row[3])

            total = total + amount

    file.close()

    print("\n----- Total Expense -----")
    print("Total Amount Spent: ₹", total)


# Main program
def main():

    # Create the CSV file
    create_file()

    while True:

        print("\n======================")
        print("    EXPENSE TRACKER")
        print("======================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            show_total()

        elif choice == "4":

            print("Thank you for using Expense Tracker!")
            break

        else:

            print("Invalid choice. Please try again.")


# Start the program
main()

