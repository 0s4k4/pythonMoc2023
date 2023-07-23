name = input("Please tell me your name: ")


if name != "Jerry":
    
    portions = int(input("How many portions of soup? "))
    price = 5.90
    total_cost = portions * price
    print(f"The total cost is {total_cost}")
    print("Next please! ")

else:
    print("Next please!")