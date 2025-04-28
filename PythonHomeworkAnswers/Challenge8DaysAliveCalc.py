#Varibles
DAYSINAYEAR: int = 365

Name: str = None
Age: int = None
Year: int = None

#Functions
def collectDetails():
    global Name
    global Age
    global Year
    
    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))
    Year = int(input("Current year: "))
    
#Runtime

collectDetails()

yearsAliveFor = Age
daysAliveFor = yearsAliveFor * 365
hoursAliveFor = daysAliveFor * 24
minsAliveFor = hoursAliveFor * 60
secondsAliveFor = minsAliveFor * 60

print(f"{Name} has been alive for {yearsAliveFor} years\n{daysAliveFor} days\n{hoursAliveFor} hours\n{minsAliveFor} minutes\n{secondsAliveFor} seconds\n** All to closest year per requirements**")
