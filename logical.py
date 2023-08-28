# and or Or oprator in python

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_high_income and not has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
