user_diagonosis = input("What's your problem?")
print(user_diagonosis)

prompt_user = input("Have you had this problem before (yes or no)?")
print(prompt_user)

if prompt_user.lower() == "yes":
    print("Well, you have it again.")

else:
    print("Well, you have it now")
