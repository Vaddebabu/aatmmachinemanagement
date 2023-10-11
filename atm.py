username="babu"
password="kohli@123"
c_name=input("enter your user name:")
c_password=str(input("enteryour password:"))
if c_name==username and c_password==password:
    print('''
          1.deposite
          2.withdraw
          3.ministatement
          4.exit
          ''')
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount"))
        amount+=dep
        print("total amount",amount)
    elif option ==2:
        withdr=int(input("enter the amount:"))
        amount-=withdr
        print("total amount",amount)
    elif option==3:
        print("==========ATM========")
        print("username:",username)
        print("total amount:",amount)
        print("thanks for visiting")
        print("==========ATM========")
    elif option==4:
        print("thanks for visiting")
else:
    print("please enter a correct login details")
        