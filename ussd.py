balance = 2000

code = input("Dial USSD code: ")
while code != "*312#":
    print("Invalid code. Try again.")
    code = input("Dial USSD code: ")

buy_again = "1"

while buy_again == "1":

    print("\n--- MTN Data Plans ---")
    print("1. Daily Plans")
    print("2. Weekly Plans")
    print("3. Monthly Plans")
    category = input("Reply with option: ")

    while category != "1" and category != "2" and category != "3":
        print("Invalid option. Try again.")
        category = input("Reply with option: ")

    if category == "1":
        print("\n--- Daily Plans ---")
        print("1. 100MB - N100")
        print("2. 200MB - N200")
    elif category == "2":
        print("\n--- Weekly Plans ---")
        print("1. 750MB - N500")
        print("2. 1.5GB - N1000")
    else:
        print("\n--- Monthly Plans ---")
        print("1. 3GB - N1500")
        print("2. 6GB - N2500")

    plan = input("Reply with option: ")

    while plan != "1" and plan != "2":
        print("Invalid option. Try again.")
        plan = input("Reply with option: ")

    if category == "1" and plan == "1":
        mb = "100MB"
        price = 100
    elif category == "1" and plan == "2":
        mb = "200MB"
        price = 200
    elif category == "2" and plan == "1":
        mb = "750MB"
        price = 500
    elif category == "2" and plan == "2":
        mb = "1.5GB"
        price = 1000
    elif category == "3" and plan == "1":
        mb = "3GB"
        price = 1500
    else:
        mb = "6GB"
        price = 2500

    print(f"\nYou are about to buy {mb} for N{price}")
    print("1. Confirm")
    print("2. Cancel")
    confirm = input("Reply with option: ")

    if confirm == "1":

        attempts = 0
        pin = input("Enter your PIN: ")

        while pin != "1234" and attempts < 2:
            attempts = attempts + 1
            print("Wrong PIN. Try again.")
            pin = input("Enter your PIN: ")

        if pin == "1234":
            if balance >= price:
                balance = balance - price
                print(f"\nYou have successfully purchased {mb} of data.")
                print(f"Your new balance is N{balance}")
            else:
                print("Insufficient airtime balance.")
        else:
            print("Too many wrong attempts.")
            buy_again = "2"
    else:
        print("Transaction cancelled.")

    if buy_again == "1":
        buy_again = input("\nBuy another plan? 1. Yes  2. No: ")

print("Thank you for using MTN.")
