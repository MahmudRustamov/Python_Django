"""Masala. 20 bal.
    Talabalar imtihondan olingan ballari list shaklida berilgan.

    grades = [45, 78, 90, 65, 88, 55, 92, 70]

    Eng yuqori va eng past ballni toping.
    O'rtacha ballni hisoblang.
    70 dan yuqori ball olganlarni yangi list ga joylang."""

grades = [45, 78, 90, 65, 88, 55, 92, 70]
grades.sort()
best_scores = []
print(grades)

for score in grades:
    if score > 70:
        best_scores.append(score)

print("Max score is: ", grades[-1])
print("Averages score is: ", sum(grades) / len(grades))
print("Lowest score is: ", grades[0])
print("Grades that greater than 70: ", best_scores)


