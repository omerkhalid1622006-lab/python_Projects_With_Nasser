def Smart_ATM_Simulator(input_PIN):
    PIN ="1234"
    Money = 5000
    if(input_PIN != PIN):
        return "Stop! PIN not correct"
    elif(input_PIN == PIN):
        Chooose_Operation = input('Please Choose the Operation (Withdraw ==> Enter 1) , (Cheak Money ==> Enter 2)')
        if(Chooose_Operation == "2"):
            return f" Your Money is {Money}"
        elif(Chooose_Operation == "1"):
            Withdraw_Money = int(input('Please Enter the Money Want to Withdraw'))
            if(Withdraw_Money > Money):
                return " Sorry , your money is not enough"
            elif(Withdraw_Money <= Money):
                return f"Done and now your money is {(Money - Withdraw_Money)}"
            
input_PIN = input('Please Enter Your PIN')
print(Smart_ATM_Simulator(input_PIN))