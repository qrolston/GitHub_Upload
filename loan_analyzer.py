#coding: utf-8
import csv
from pathlib import Path
import pathlib

from matplotlib.pyplot import get

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
total_loans = len(loan_costs)
print('The total number of loans in the list is',total_loans)
# What is the total of all loans? ANSWER = 5
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!
total_of_all_loans = sum(loan_costs)
print('The total of all loans in the list is', total_of_all_loans)

#What is the total of all loans? ANSWER = 2750

# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
average_loan_price = total_of_all_loans/total_loans
print('The average loan price is',average_loan_price)
# What is the average loan amount from the list? ANSWER = 550
"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

loan_price = loan.get("loan_price")
print(f"loan_price =",loan_price)
remaining_months = loan.get("remaining_months")
print(f"remaining_months =",remaining_months)
future_value = loan.get("future_value")
print(f"future_value =", future_value)

# ANSWER loan_price = 500 remaining_months = 9 future_value = 1000

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!
discount_rate = .2
print(f"discount_rate =", discount_rate)
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"present_value =", present_value)

# ANSWER discount_rate = 0.2 present_value = 861.7727126032183

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if present_value >= loan_price :
    print("Buy this loan its a deal!")
else:
    print("Do not buy loan, bad investment")

#ANSWER "Buy this loan its a deal!" It makes sense to buy this loan at the current price
"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate): 
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months 
    return present_value
    
# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!


loan_price = new_loan.get("loan_price")
print(f"loan_price =",loan_price)
remaining_months = new_loan.get("remaining_months")
print(f"remaining_months =",remaining_months)
repayment_interval = new_loan.get("repayment_interval")
print(f"repayment_interval =",repayment_interval)
future_value = new_loan.get("future_value")
print(f"future_value =", future_value)


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
annual_discount_rate = 0.2

present_value = calculate_present_value( new_loan["future_value"], new_loan["remaining_months"], 0.20)

print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
# inexpensive_loans = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
inexpensive_loans=[]
# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for item in loans:
    # loan_price = item["loan_price",0]
    if int(loans(0)) > 500: 
            inexpensive_loans.append(loans[0])

    # if loan_price <= 500:
    #         inexpensive_loans.append(loan_price)
    #         # inexpensive_loans.append[loans(0),loans(1),loans(2),loans(3)]
            
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print(f"inexpensive_loans list",inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_values"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.


# open the file in the write mode

with open(output_path,"w",newline='') as file:
    # create the csv writer
    csvwriter = csv.writer(file)

    #write a header to the csv file
    csvwriter.writerow(header)
    # for row in inexpensive_loans :
    #     csvwriter.writerow(row)
    # write a row to the csv file
    csvwriter.writerows(inexpensive_loans)

    
# with open(write_file_path, 'w') as f:
#     csv_writer=csv.writer(f, delimiter='|')
#     # for each_row in tall_list: 
#     #     csv_writer.writerow(each_row) # ['onix', '2100']
#     csv_writer.writerows(tall_list)