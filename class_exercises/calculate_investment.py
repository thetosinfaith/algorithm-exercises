
deposit = float(input("enter your amount"))
for i in range(1,31):
    roi = deposit * 0.10
new_amount = deposit + roi
deposit = new_amount
print(f"Your roi is ${roi:.2f},your investment is now ${new_amount:.2f} in year {i}")