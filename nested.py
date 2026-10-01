credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your annual income: "))

if credit_score > 700:
    if income > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low")