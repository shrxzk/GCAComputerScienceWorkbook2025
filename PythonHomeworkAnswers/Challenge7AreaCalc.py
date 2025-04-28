#Functions
def calculateSize(x,y,z):
    #Area or Volume
    if x and y and z:
        return x * y * z
    else:
        return "Not a valid input"
    
#Runtime
print("Room size calculator")
print("1. Area calculator")
print("2. Volume calculator")
print("Otherwise exit")

response: str = input("\n")

if response == "1":
    x: float = float(input("X axis: "))
    y: float = float(input("Y axis: "))
    answer = calculateSize(x, y, 1.0)
    print(f"Area = {answer}")
elif response == "2":
    x: float = float(input("X axis: "))
    y: float = float(input("Y axis: "))
    z: float = float(input("Z axis: "))
    answer = calculateSize(x, y, z)
    print(f"Volume = {answer}")
else:
    exit