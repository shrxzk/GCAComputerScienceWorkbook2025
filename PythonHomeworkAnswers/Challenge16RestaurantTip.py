#Varibles
TAXICOSTPERMILE: float = 0.45

NumberOfPeople: int = None
DistanceToTravel: float = None

#Functions
def caclulateCost(numberOfPeople):
    cost = (100 * 1.15)
    individualCost = (cost / numberOfPeople)
    
    return individualCost

def calculateTaxi(distance):
    global TAXICOSTPERMILE
    TaxiCost = (distance * TAXICOSTPERMILE)
    
    return int(TaxiCost)

#Runtime
print("Restruant Tip\n")

NumberOfPeople = int(input("Number of people: "))
DistanceToTravel = float(input("Distance home in miles: "))

print(f"\nTrip out cost:\nOverall cost of night is {((100 * 1.15) + calculateTaxi(DistanceToTravel)): .2f}\nMeal cost with tip is {(100 * 1.15): .2f}\nCost of taxi is{calculateTaxi(DistanceToTravel): .2f}\nCost per person is {caclulateCost(NumberOfPeople): .2f}")