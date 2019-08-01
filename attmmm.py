userid=input("enter the id::")
pin=input("enter the 4 digit pin::")
data=["santhiya","4321"]
if(userid and pin in data):
  print("valid")
else:
  print("invalid")
  exit;
  def valid():
    if(valid): 
        def balance():
          amt=int(input("entire amount::"))
          print("amt")
          balance()
        def withdrawl():
          amt=int(input("what amount of withdrawl::"))
          print("new balance",balance-amt)
          withdrawl()
        def deposit():
            amt=int(input("what amount of deposit::"))
        print("new balance",balance+amt)
        deposit()
        choice=int(input("choose an option:1.balance 2.withdrawl 3.deposit"))
        if choice==1:
            print(balance);
        elif choice==2:
            print(withdrawl);
        else: 
            print(deposit);
            return

        def current():
                amt=int(input("recently add amount:0"))
                print("new balance",balance+amt)
                current()
                def savings():
                  amt=int(input("already saved amount:"))
                  print("new balance")
                  savings()
                  choice=int(input("choose an option:1.current 2.savings"))
                  if choice==1:
                    print(current);
                  elif choice==2:
                      print(savings);
                  else:
                        print(exit);
                        return
                       
print("transaction has been successful");
