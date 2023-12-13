print("\t\t\t Welcome to Pizza Hut!!!")
print("\t\t\t-------------------------")
print("\n")
print("\t\t\t\t MENU")
print("\t\t\t\t-------")
print("\n")
print(" PIZZAS \t\t\t\t\t TOPPINGS")
print("--------\t\t\t\t\t------------ ")
print("1.Margherita Pizza - Rs.90 \t\t\t1.Pepporoni - Rs.40 \n2.Preppy Paneer Pizza - Rs.100 \t\t\t2.Cheese - Rs.30 \n3.Pepper Barbeque Chicken Pizza - Rs.140\t3.Chicken - Rs.80 \n4.Tandoori Pizza - Rs.180")
pepporoni=40
cheese=30
chicken=80
Margherita_Pizza=90
Preppy_Paneer_Pizza=100
Pepper_Barbeque_Chicken_Pizza=140
Tandoori_Pizza=180


a=str(input("\nWould you like to order pizza? (yes/no):"))
if a=="yes":
    b=int(input("What pizza would you like to order? "))
    if b==1:
        print("Margherita Pizza")
        c=str(input("\nWhat toppings do you need?"))
        if c=="pepporoni":
            sum=Margherita_Pizza+pepporoni
            print("\nYour total cost is:",sum)
            print("\nYour order of Margherita Pizza with pepporoni topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='cheese':
            sum=Margherita_Pizza+cheese
            print("\nYour total cost is:",sum)
            print("\nYour order of Margherita Pizza with cheese topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='chicken':
            sum=Margherita_Pizza+chicken
            print("\nYour total cost is:",sum)
            print("\nYour order of Margherita Pizza with chicken topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
    
    elif b==2:
        print("Preppy Paneer Pizza")
        c=str(input("\nWhat toppings do you need?"))
        if c=="pepporoni":
            sum1=Preppy_Paneer_Pizza+pepporoni
            print("\nYour total cost is:",sum1)
            print("\nYour order of Preppy Paneer Pizza Pizza with pepporoni topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='cheese':
            sum1=Preppy_Paneer_Pizza+cheese
            print("\nYour total cost is:",sum1)
            print("\nYour order of Preppy Paneer Pizza Pizza with cheese topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='chicken':
            sum1=Preppy_Paneer_Pizza+chicken
            print("\nYour total cost is:",sum1)
            print("\nYour order of Preppy Paneer Pizza with chicken topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
    elif b==3:
        print("Pepper Barbeque Chicken Pizza")
        c=str(input("\nWhat toppings do you need?"))
        if c=="pepporoni":
            sum2=Pepper_Barbeque_Chicken_Pizza+pepporoni
            print("\nYour total cost is:",sum2)
            print("\nYour order of Pepper Barbeque Chicken Pizza with pepporoni topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='cheese':
            sum2=Pepper_Barbeque_Chicken_Pizza+cheese
            print("\nYour total cost is:",sum2)
            print("\nYour order of Pepper Barbeque Chicken Pizza with cheese topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='chicken':
            sum2=Pepper_Barbeque_Chicken_Pizza+chicken
            print("\nYour total cost is:",sum2)
            print("\nYour order of Pepper Barbeque Chicken Pizza with chicken topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
    elif b==4:
        print("Pepper Tandoori Pizza")
        c=str(input("\nWhat toppings do you need?"))
        if c=="pepporoni":
            sum3=Tandoori_Pizza+pepporoni
            print("\nYour total cost is:",sum3)
            print("\nYour order of Pepper Tandoori Pizza with pepporoni topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='cheese':
            sum3=Tandoori_Pizza+cheese
            print("\nYour total cost is:",sum3)
            print("\nYour order of Pepper Tandoori Pizza with cheese topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
        elif c=='chicken':
            sum3=Tandoori_Pizza+chicken
            print("\nYour total cost is:",sum3)
            print("\nYour order of Pepper Tandoori Pizza with chicken topping is placed")
            print("\n\t\tThank you for visiting our shop, Come again!!!")
    else:
        print("\n!!!Enter correct menu number!!!")
else:
    exit












































































































































































    
          
          
          
