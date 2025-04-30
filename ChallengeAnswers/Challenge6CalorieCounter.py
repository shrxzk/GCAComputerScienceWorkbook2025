#Varibles
MALECALORIES: int = 2500
FEMALECALORIES: int = 2000

CurrentCalories: int = None
Name: str = None
Gender: str = None
CaloriesToDisplay: int = 0

#Functions
def checkValidDetails(Gender, Calories, Name):
    if (Gender == "male" or Gender == "female") and Calories > 0 and len(Name) > 1:
        global CaloriesToDisplay
        if Gender == "male":
            CaloriesToDisplay = MALECALORIES - CurrentCalories
        elif Gender == "female":
            CaloriesToDisplay = FEMALECALORIES - CurrentCalories
        else:
            print("Logic Error")
            return True
        return False
    else:
        print("Enter a valid details")
        return True

#Runtime

while True:
    Name: str = input("Enter your name: ")
    Gender: str = (input("Enter your gender: ")).lower()
    CurrentCalories: int = int(input("How many calories have you eaten today?\n"))
    Error = checkValidDetails(Gender, CurrentCalories, Name)
    if not Error:
        break



print()
print("Details collected")
print()

print(f"{Name}'s calorie counter:\nYou can eat {CaloriesToDisplay} more calories today\n")

#Made by yk who


