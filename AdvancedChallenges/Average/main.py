#Libary
#None required

#Declarations
currentNumbers: int = 0
totalNumbers: int = 0

#Functions
def collect_num() -> None:
    global totalNumbers
    global currentNumbers
    currentNumbers += int(input("Enter a number: "))
    totalNumbers += 1

def query_end() -> None:
    if input("Continue? y/n ").lower() == "n":
        print(f"Average is [{currentNumbers / totalNumbers}]")
        exit()
    else:
        return

#Runtime
while True:
    collect_num()
    query_end()