from os import system

system('cls')

while True:
    print("|********************************|")
    print("|   Welcome to the BalladDrinks  |")
    print("|********************************|")
    print("|Enter the option you want to choose|\n" +
          "|1 - Track                       |\n" +
          "|2 - VIP                         |\n" +
          "|3 - Exit                        |"
          )

    track_price = 150.00
    vip_price = 250.00

    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"You chose the Track option for ${track_price:.2f}.")
        is_student = input("Are you a student? (Y/N): ").strip().lower()
        if is_student == 'y':
            discount = track_price * 0.5  # 50% discount for students on Track
            print(f"You received a 50% discount. Amount to pay: ${discount:.2f}")
        else:
            discount = track_price
            print(f"Amount to pay: ${track_price:.2f}")
    elif choice == '2':
        print(f"You chose the VIP option for ${vip_price:.2f}.")
        is_student = input("Are you a student? (Y/N): ").strip().lower()
        if is_student == 'y':
            discount = vip_price * 0.5  # 50% discount for students on VIP
            print(f"You received a 50% discount. Amount to pay: ${discount:.2f}")
        else:
            discount = vip_price
            print(f"Amount to pay: ${vip_price:.2f}")
    elif choice == '3':
        print("Exiting")
        break
    else:
        print("Invalid option. Please try again.")

    age = int(input("Enter your age: "))

    if age >= 18:
        print("Access Granted. You are of legal age.")
        if age >= 60:
            additional_discount = discount * 0.05  # 5% additional discount for seniors over 60
            discount -= additional_discount  # Apply additional discount
            print(f"You got an additional 5% discount. Amount to pay: ${discount:.2f}")
    else:
        print("Access Denied. You aren't of legal age.")
