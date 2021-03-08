# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


subject_scores = [
    ('English', 88),
    ('Science', 90),
    ('Maths', 97),
    ('Social sciences', 82)
]


# subject_scores.sort(key=lambda score: score[1])
# print(subject_scores)

sorted_subject_scores = sorted(subject_scores, key=lambda score: score[1])
print(sorted_subject_scores)
