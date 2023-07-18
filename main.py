#Part A: house hunting
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

def houseHunting(total_cost, annual_salary, portion_saved, semi_annual_raise):
    number_of_months = 1
    portion_down_payment = total_cost*(25/100)
    rate_of_return = (4/100)
    monthly_savings = 0
    monthly_salary = annual_salary/12
    multiplicand = 6*1
    product = multiplicand
    months = True
    while(months):
       investing = monthly_savings + (monthly_savings*(rate_of_return/12))
       monthly_savings = investing + monthly_salary*portion_saved
        if(portion_down_payment>= monthly_savings):
            number_of_months+=1
            #product = multiplicand
            if(number_of_months == product):
                monthly_salary+= + monthly_salary*semi_annual_raise
                #monthly_savings = monthly_salary
                product+=multiplicand
        else:
            months=False
            print(number_of_months, "number of years that would take to save for down payment.")
    return(number_of_months)
houseHunting(float(input()), float(input()), float(input()), float(input()))

#part C: Finding the right (best saving rate) amount to save away for a down payment in 36 months or less. (Ps1c.py)

def savingRate(, ,):
    future_homeOwner=float(input())



