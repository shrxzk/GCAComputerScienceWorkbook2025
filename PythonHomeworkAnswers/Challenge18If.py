#Varibles
NumberOne: float = float(input("Enter number one: "))
NumberTwo: float = float(input("Enter number two: "))

#Runtime
if NumberOne > NumberTwo:
    print(f"{NumberOne} is greater than {NumberTwo}")
elif NumberOne < NumberTwo:
    print(f"{NumberTwo} is greater than {NumberOne}")
else:
    print(f"{NumberOne} is equal to {NumberTwo}")
    
#This challenge also works for challenge 19 as its the same code being used