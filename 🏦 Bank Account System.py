#🏦 Bank Account System
print("-------🏦 Bank Account System--------")
print("MENU: \n 1.SHOW DETAILS: \n 2.DEPOSIT MONEY: \n 3.WITHDRAW MONEY: \n 4.EXIT:")
def show_details():
    for key, value in candidate.items():
        print(key,value)
def withdrawl_money():
    a=float(input("Enter the amount: "))
    if a>candidate["balance"]:
        print("iniffucent balance🥲")
    else:
        candidate["balance"]=candidate["balance"]-a
        print("withdrawl successful🤗")
    show_details()
def deposit_money():
    b=float(input("Enter the amount: "))
    candidate["balance"]=b+candidate["balance"]
    show_details()
def Exit():
    print("--------THANK YOU-------")

candidate={
    "name":"kunal",
    "balance":50000
}
while True:
    choice=float(input("Enter the choice: "))
    if choice==1:
        show_details()
    elif choice==2:
        deposit_money()
    elif choice==3:
        withdrawl_money()
    elif choice>4:
        print("INVALID CHOICE")
    elif choice==4:
        Exit()
        break

