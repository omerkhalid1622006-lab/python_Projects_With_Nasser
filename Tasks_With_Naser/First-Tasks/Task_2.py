def Select_Junior_Python(perfect_python,Years_experiance,CIS_BootCamp):
    if(perfect_python  and (CIS_BootCamp or Years_experiance >= 2) ):
        return "Congrats"
    else:
        return  "Sorry"
    
perfect_python = input("Are you perfect in python? (Yes / No)")
Years_experiance = input("How many years of experiance")
CIS_BootCamp = input("Do you have a bachelor's degree in CIS or have any completed a Bootcamp? (Yes / No)")
print(Select_Junior_Python(perfect_python,Years_experiance,CIS_BootCamp))


