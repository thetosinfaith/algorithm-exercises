# def amcwit(first: list[int] = [3],
#            second: list[int] = [3]):
#
#
#     for i in range(list):
#         print([0], [1], [2])
#
# amcwit(first=)
# print(amcwit(len()))

v = 'A', 'M', 'C', 'W', 'I', 'T'


def africa(s, step):
    return [s[i::step] for i in range(step)]

print(africa(v, 3))
