num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)

mid_number = num1 + num2 + num3 - min_num - max_num

print("Numbers in increasing order:", min_num, mid_number, max_num)
