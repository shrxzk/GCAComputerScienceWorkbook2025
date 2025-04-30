#Runtime
print("Vowl counter!\n")
Sentence: str = input("Enter a sentence:\n")
NumberOfEs: int = 0

for letter in Sentence.lower():
    if letter in ("a","e","i","o","u"):
        NumberOfEs += 1

print(f"\nThe numbers of e's in the sentence is: {NumberOfEs}")