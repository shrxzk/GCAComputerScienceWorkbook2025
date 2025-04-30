NAME = None #ENTER YOUR NAME

while NAME != "John":
    NAME = input("Enter first name: ").capitalize()
    if NAME != "John":
        print("Are you sure?\n")
        
print(f"Welcome {NAME}")