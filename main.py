# Part A: house hunting ps1a.py
# how many months needed to save enough for down payment?
"""
def houseHunting(annual_salary, portion_saved, total_cost):
    number_of_months = 0
    portion_down_payment = total_cost*(1/4)
    r = (1/25)
    current_savings = 0
    investments = 0
    notEnough = True

    while notEnough:
        current_savings += investments + ((annual_salary*portion_saved)/12)
        investments = (current_savings*r)/12
        number_of_months +=1

        if current_savings >= portion_down_payment:
            notEnough = False
    print(f'Number of months to save for down payment {number_of_months} or {number_of_months/12} years')


print("Please enter your annual income: ")
annual_salary = float(input())
print("Please enter the percentage to be saved every month: ")
portion_saved = float(input())
print("Please enter the current cost of the house: ")
total_cost = float(input())
houseHunting(annual_salary, portion_saved, total_cost)
"""

# Code ps1a.py works as intended.


# Part B: Saving for down payment, with a percentage raise every six months ps1b.py

"""def houseHunting(annual_salary, portion_saved, total_cost, semi_annual_raise):
    number_of_months = 0
    portion_down_payment = total_cost*(1/4)
    r = (1/25)
    current_savings = 0
    investments = 0
    notEnough = True

    while notEnough:
        current_savings += investments + ((annual_salary*portion_saved)//12)
        investments = (current_savings*r)//12
        number_of_months +=1

        if number_of_months%6 == 0:
            annual_salary = annual_salary + (annual_salary*semi_annual_raise)

        if current_savings >= portion_down_payment:
            notEnough = False
    print(f'Number of months to save for down payment {number_of_months} or {number_of_months//12} years')


print("Please enter your annual income: ")
annual_salary = float(input())
print("Please enter the percentage to be saved every month: ")
portion_saved = float(input())
print("Please enter the current cost of the house: ")
total_cost = float(input())
print("Enter semi-annual percentage raise: ")
semi_annual_raise = float(input())
houseHunting(annual_salary, portion_saved, total_cost, semi_annual_raise)"""


"""
Online code for REFERENCE only

running = True
while True:
    try:
        base_annual_salary = float(input("Enter your annual salary: "))
        break

    except ValueError:
        print("Please type float or integers only.")


total_cost = 1000000  
percent_down_payment = 0.25  
monthly_r = 0.04 / 12  
semi_annual_raise = 0.07  
down_payment = total_cost * percent_down_payment
months = 36  
epsilon = 100  
initial_high = 10000 
high = initial_high  
low = 0 
current_savings = 0
step = 0 
portion_saved = (high + low) // 2

while abs(current_savings - down_payment) > epsilon:
    step += 1
    current_savings = 0
    annual_salary = base_annual_salary
    monthly_salary = annual_salary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)

    for month in range(1, months + 1):
        current_savings += (current_savings * monthly_r)
        current_savings += monthly_deposit
        if month % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)

    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved

    portion_saved = int(round((high + low) / 2))
    if prev_portion_saved == portion_saved:
        break

print()
if portion_saved == initial_high:
    print("Not possible to acquire the house within 36 months.")
else:
    print("Best savings rate: {}".format(round(portion_saved / 10000, 4)))
    print("Steps in Bisection search: {}".format(step))

# Code ps1b.py works as intended.
"""


# part C: Finding the best rate of saving to pay the house in 3 years. ps1c.py
# In other words, what percentage of my monthly salary needs to be save to achieve the goal.

annual_salary = int(input("Enter you annual salary: "))
house_cost = int(input("Enter Market Value of The House: "))
stepCount = 0
upper_bound_limit = 36
return_on_investment = (1 / 25)/12
semi_annual_raise = 7 / 100
down_payment = house_cost * (1 / 4)
upper = 10000
lower = 0
salary = annual_salary/12
monthly_savings = 0

while abs(monthly_savings -  down_payment) > 100:
    monthly_savings = 0
    investment = 0
    interest_rate = ((upper + lower)/10000) / 2
    salary *= interest_rate
    for month in range(1, upper_bound_limit + 1):
        monthly_savings += investment + salary
        investment = monthly_savings * return_on_investment
        if month % 6 == 0:
            salary += (salary * semi_annual_raise)
    stepCount += 1

    if monthly_savings > down_payment:
        upper = interest_rate
    else:
        lower = interest_rate
"""
if interest_rate < lower:
    print("not enough mula")
else:
   print("you will buy the dang house.", "%.4f" % interest_rate, stepCount)
"""