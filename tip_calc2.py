bill_amount = int(input("Total bill amount? "))
level_of_service = input("Level of service? ")
bill_split = int(input("Split how many ways? "))

lower_los = level_of_service.lower()
tip = 0

# Good -> 20%
# Fair -> 15%
# Bad -> 10%

if lower_los == 'good':
    tip = .20
elif lower_los == 'fail':
    tip = .15
elif lower_los == 'bad':
    tip = .10
else:
    print('Invalid Input')

total = (bill_amount * tip) + bill_amount
total_split = total / bill_split
print("Tip amount: $%.2f" % (tip * 100))
print("Total amount: $%.2f" % total)
print("Amount per person: $%.2f" % total_split)
