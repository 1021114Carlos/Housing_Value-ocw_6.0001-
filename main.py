#Part A: house hunting (ps1a.py)
#how many months needed to save enough for down payment?

def houseHunting(annual_salary, portion_saved, total_cost):
    number_of_months = 0
    portion_down_payment = total_cost*(25/100)
    r = (4/100)
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

#Part B: Saving for down payment, with a percentage raise every six months (Ps1b.py)

def houseHunting(annual_salary, portion_saved, total_cost, semi_annual_raise):
    number_of_months = 0
    portion_down_payment = total_cost*(25/100)
    r = (4/100)
    current_savings = 0
    investments = 0
    notEnough = True
    
    while notEnough:
        current_savings += investments + ((annual_salary*portion_saved)//12)
        investments = (current_savings*r)//12
        number_of_months +=1
        
        if number_of_months%6 == 0:
            annual_salary = annual_salary + ((annual_salary*semi_annual_raise)//2)
            
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
houseHunting(annual_salary, portion_saved, total_cost, semi_annual_raise)

#part C: Finding the right (best saving rate) amount to save away for a down payment in 36 months or less. (Ps1c.py)

def savingRate(, ,):
    future_homeOwner=float(input())



