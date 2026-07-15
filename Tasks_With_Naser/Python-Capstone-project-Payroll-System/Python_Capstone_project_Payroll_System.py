# 1. Function to calculate performance bouns
def calculate_bonus(base_salary,performance_rating):
    if(performance_rating == 5):
        return 0.20*base_salary
    elif(performance_rating in [3,4]):
        return 0.10*base_salary
    else:
        return 0.0 * base_salary
    
# 2. Function to calculate progressive tax deductions    
def calculate_tax(gross_salary):
    if (gross_salary > 7000):
        return 0.15 * gross_salary
    elif (3000<gross_salary<7000):
        return 0.10 * gross_salary
    else:
        return 0.0 * gross_salary
    
# 3. Core runtime app    
def main_hr_app():
    print("Corporate Payroll System")
    
    # User input
    employee_name = input("Please Enter Your name :")
    employee_department = input("Please Enter Your department :")
    base_salary = float(input("Please Enter Your Salary (EGP) :"))
    performance_rating = int(input("Please Enter Your rating (1:5) :"))

    #Input Validation
    if (performance_rating > 5 or performance_rating < 1 or base_salary < 0):
        print(" Not Support You , Please restart and check your input.")
        return 
    
    # Process Flow Via Function
    bonus = calculate_bonus(base_salary,performance_rating)
    gross_salary =base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax

    # Bonus Status
    if performance_rating == 5:
        performance = "Excellent"

    elif performance_rating in [3, 4]:
        performance = "Good"

    else:
        performance = "Needs Improvement"

    # Output Statement Generator
    print(f" Payroll System for: {employee_name} with department: {employee_department}")
    print(f"Performance : {performance}")
    print(f"Base Salary: {base_salary:.2f} EGP")
    print(f"Earned Bouns: {bonus:.2f} EGP")
    print(f"Tax Deduction: {tax:.2f} EGP")
    print("*" * 5)
    print(f"Net Payable Cash: {net_salary:.2f} EGP")
    print(f"Thanks For Using Eng {employee_name}")

# Program run
main_hr_app()
