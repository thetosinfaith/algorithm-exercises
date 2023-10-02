user_input = input("Enter a score: ")


def average_scores(scores):
    return sum(scores) / len(scores)

    exam_scores = []
    for i in range(10):
        score = int(input("Enter your score: "))
        exam_scores.append(score)


print(average_scores(21))
