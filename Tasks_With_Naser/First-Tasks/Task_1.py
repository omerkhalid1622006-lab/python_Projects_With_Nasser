def Instant_Discount_System(input_money):
    First_discount = 0 
    Second_discount = 0.10
    Third_discount = 0.20
    if(input_money < 100):
        return f"Your_discount is {First_discount} and total after discount is {(First_discount * input_money)}"
    elif(100 <= input_money < 500):
        return f"Your_discount is {Second_discount} and total after discount is {(Second_discount * input_money)}"
    else:
        return f"Your_discount is {Third_discount} and total after discount is {(Third_discount * input_money)}"

print("Hi my Friend")
input_money = float(input("Please Enter Money"))
print(Instant_Discount_System(input_money))