#Runtime
choice: str = input("Are you male or female? ").lower # We use lower backend

if choice in ("m", "male"):
    print("We have discounts for men")
elif choice in ("f", "female"):
    print("We have discounts for women")
elif choice not in ("m","male","f","female"):
    print("Sorry not a valid choice") #This is a pointless line of code as we could just use else?
    
#I couldnt find the question so i just compiled the page into one file