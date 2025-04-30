#Extention
#Libarys
from datetime import date

#Runtime
print("School dinner calculator\n")

StartingAmount: float = float(input("Starting amount: £"))
TodaysCost: float = float(input("Todays cost: £"))

EvaluatedCost: float = StartingAmount - TodaysCost

print()
print(f"At {date.today()} you have £{EvaluatedCost} left on your account")