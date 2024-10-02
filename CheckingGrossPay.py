# Prompt the user for hours worked
hours = input("Enter Hours: ")
hours = float(hours)

# Prompt the user for rate per hour
rate = input("Enter Rate: ")
rate = float(rate)

# Calculate gross pay
gross_pay = hours * rate

# Print the gross pay
print("Pay:", gross_pay)
