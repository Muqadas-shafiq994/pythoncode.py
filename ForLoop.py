#  For LOOP
a="hello"
for i in a:
    print(i)
# Assignment of ticket peice
input_ages= input("Enter your age:")
ages= [int(age.strip()) for age in input_ages.split(',')]
for k in ages:
    if k<=3:
        print(f"your age is {k} and you have 'zero' ticket price ")
    elif k<=7:
        print(f"your age is {k} and your ticket price is '10000' ")
    elif k<= 18:
        print(f"your age is {k} and your ticket price is '25000'")
    elif k<=50:
        print(f"your age is {k} and your ticket price is '45000'")
    else:
        print("your input is invalid. Try again")