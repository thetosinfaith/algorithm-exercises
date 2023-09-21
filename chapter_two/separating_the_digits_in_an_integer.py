user_input = int(input("Please enter a five digit number: "))

a = user_input % 10
user_input = user_input // 10
print(a, user_input)

b = user_input % 10
user_input = user_input // 10
print(b, user_input)

c = user_input % 10
user_input = user_input // 10
print(c, user_input)

d = user_input % 10
user_input = user_input // 10
print(d, user_input)

e = user_input % 10
user_input = user_input // 10
print(e, user_input)


print(e, d, c, b, a, sep="    ")
