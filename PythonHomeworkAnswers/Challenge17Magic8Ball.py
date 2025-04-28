#Libarys
import random

#Varibles
Answers = {
    1 : "Absolutley!",
    2 : "No way Pedro!",
    3 : "Go for it tiger.",
    4 : "Im not to sure.",
    5 : "Definetly not."
} #This is a dictonary data structure

#Runtime
print("\nWelcome to the magic 8 ball game!\nUse it to answer your questions\n")

question: str = input("\nAsk me for any advice and I'll help you out. Type in your question and then press Enter for an answer.\n")

print("\nShaking.... \n" * 4)

choice = random.randint(1, len(Answers))

print(Answers[choice])

#I modifeied the code from the question to prioritize efficeny 