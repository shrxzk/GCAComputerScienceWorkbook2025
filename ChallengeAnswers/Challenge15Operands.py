NumberOne: float = 3.123456789
NumberTwo: float = 9.876543210
NumberThree: float = 1.1

Answer = (NumberOne * NumberTwo)

print(f"{Answer: .3f}")

print("%0.2f"% (NumberThree))
#One prints : 30.848955941126352
#Two prints : 30.849
#Three prints : 1.10