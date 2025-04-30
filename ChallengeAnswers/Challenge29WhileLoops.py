number = 100

while number > 10 or number < 0:
    number = int(input("Please enter a number between 1 and 10"))
    
print(f"Your number multiplied by 10 is: {number*10}")

#The int is nessisary as you cant muliply a string by a number