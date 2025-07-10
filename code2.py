#if/else statment

age=int(input("Enter age:"))
ticket_price=int(input("Enter ticket price:"))

if age<=3:
    if ticket_price==0:
        print("you are a child")
    else:
        print("you are not a child")
elif age<=6:
    if ticket_price<=30000:
        print("you are toddler")   
    else:
        print("you are not a toddler")
elif age<=15:
    if ticket_price<=60000:
        print("You are teenager")
    else:
        print("you are not teenager")
elif age<=20:
    if ticket_price<=70000:
        print("you are young adult") 
    else:
        print("you are not young aduit") 
elif age<=80:
    if ticket_price<=90000:
        print("you are adult") 
    else:
        print("you are not adult")  
else:
    print("your age is not correct")         

    