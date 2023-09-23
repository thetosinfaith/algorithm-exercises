for i in range(1, 51):

    if i % 5 and i % 3:
        print('fuzzBuz')
    else:


        if i % 3 == 0:
         print("Fizz")
        else:


            if i % 5 == 0:
                print("Buzz")

            else:
                print(i)


            # if i % 3 % 5 == 0:
            #     print("FizzBuzz")
