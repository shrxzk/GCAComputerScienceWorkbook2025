#Functions
def checkValidity(AmountSpent):
    if AmountSpent > 20:
        return "a £3 voucher."
    elif AmountSpent > 10:
        return "a £1 voucher."
    else:
        return "no voucher."

#Runtime
AmountSpent: float = float(input("How much has the customer spent today? £"))

print(f"\nIssue the customer {checkValidity(AmountSpent)}\n")
