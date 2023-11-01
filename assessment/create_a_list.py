from typing import List


# def list_name(f):
#     score = []
#
#
# for numbers in range(1, 21):
#     score.append(numbers)
# print(score)
def odd_number():
    numbers = []
    for i in range(1, 21):
        if i % 2 != 0:
            numbers.append(i)
    return numbers


print(odd_number())
