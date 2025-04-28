#Dict
Messages = {
    1 : "You seem really sad whats wrong?",
    2 : "The days not over yet.",
    3 : "You better feel better soon.",
    4 : "Things are looking up.",
    5 : "We all in the sameboat.",
    6 : "Todays a nice day isnt it.",
    7 : "The weather looks nice.",
    8 : "You seem happy today!",
    9 : "Your are well happy!",
    10 : "Your very happy bro."
} 

#Functions
def checkHappy(rating):
    if rating > 0 and rating < 10:
        return Messages[rating]
    else:
        print("[E-01] Number falls out of range")
        
#Runtime
Happines: int = int(input("\nHow happy are you feeling on a scale of 1-10: "))

print(f"\n{checkHappy(Happines)}\n")