def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

# Prompt the user for hours worked
hours = input("Enter Hours: ")
hours = float(hours)

# Prompt the user for rate per hour
rate = input("Enter Rate: ")
rate = float(rate)

# Compute the pay using the computepay function
pay = computepay(hours, rate)

# Print the computed pay in the required format
print("Pay", pay)
