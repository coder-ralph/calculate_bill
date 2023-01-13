# Constant values
LOWER_INCOME_MAX = 24164
UPPER_INCOME_MIN = 144984

# Variables
total_bill = 0
food_percentage = 0
water_percentage = 0
electricity_percentage = 0
transportation_percentage = 0
savings = 0
income_class = ""

# Inputs
income = float(input())
food = float(input())
water = float(input())
electricity = float(input())
transportation = float(input())

# Compute the total bill
total_bill = food + water + electricity + transportation
# Determine the percentages of each category
food_percentage = (food / total_bill) * 100
water_percentage = (water / total_bill) * 100
electricity_percentage = (electricity / total_bill) * 100
transportation_percentage = (transportation / total_bill) * 100

# Determine the difference of income and total bill
savings = income - total_bill

# If income is lower than x
if income <= LOWER_INCOME_MAX:
  income_class = "Lower income class"
elif income > LOWER_INCOME_MAX and income < UPPER_INCOME_MIN:
  # If income is greater than x (lower) but less than y (upper)
  income_class = "Middle income class"
else:
  income_class = "Upper income class"

# Print the summary. Make sure to convert the float into strings and format the percentages to 2 decimal places.
print("SUMMARY")
print("Income: " + str(income) + " - " + income_class)
print("Food: " + str(food) + " PHP (" + "{0:.2f}".format(food_percentage) + "%)")
print("Water: " + str(water) + " PHP (" + "{0:.2f}".format(water_percentage) + "%)")
print("Electricity: " + str(electricity) + " PHP (" + "{0:.2f}".format(electricity_percentage) + "%)")
print("Transportation: " + str(transportation) + " PHP (" + "{0:.2f}".format(transportation_percentage) + "%)")
print("Total bill: " + str(total_bill) + " PHP")
if savings >= 0:
  print("You are in budget and you saved " + str(savings) + " PHP.")
else:
  # Make sure to make it a positive by multiplying to -1
  print("You are in short of budget. You need " + str(savings * -1) + " PHP.")
