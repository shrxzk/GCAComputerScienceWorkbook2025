#Libarys
import math

#Varibles
PICTURES: float = 0.35
TEXTS: float = 0.10
DATA: float = 2.50
 
P_used: int = None
T_used: int = None
D_used: int = None

Total_cost: float = 0
#Functions
def evalUsage():
    global Total_cost
    
    Total_cost = ((P_used * PICTURES) + (T_used * TEXTS) + (math.ceil(D_used / 500) * 2.50))
    
    if Total_cost < 10:
        return f"\nYour monthly total bill comes to £{Total_cost}"
    else:
        return f"\nYour monthly total bill comes to £{Total_cost}\n We would advise you purchase a contract."
    #D_cost = D_used * DATA
    
#Runtime
P_used = float(input("Amount of Pictures sent: "))
T_used = float(input("Amount of Texts sent: "))
D_used = float(input("Amount of Data used mb: "))

print(f"\n{evalUsage()}")