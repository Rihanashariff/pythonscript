n1=input()
if n1==n1[::-1]:
    print("yes")
else:
    a1=n1.strip("0")
    
    if a1==a1[::-1]:
        print("yes")
    else:
        a1=n1.lstrip("0")
        
        if a1==a1[::-1]:
            print("yes")
        else:
            print("no")
