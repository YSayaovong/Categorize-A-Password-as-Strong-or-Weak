# Prompt the user for hours worked
hours = input("Enter Hours: ")
hours = float(hours)

# Prompt the user for rate per hour
rate = input("Enter Rate: ")
rate = float(rate)

# Calculate gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    # For hours above 40, pay 1.5 times the rate
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * (rate * 1.5)
    gross_pay = regular_pay + overtime_pay

# Print the gross pay, formatted to two decimal places
print(f"{gross_pay:.2f}")
