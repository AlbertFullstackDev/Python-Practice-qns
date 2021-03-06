# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

names = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    names.append(name)
    scores.append(score)

python_students = [[name, score] for name, score in zip(names, scores)]

lowest_score_array = min(python_students, key=lambda student: student[1])

lowest_score = lowest_score_array[1]


python_students = [
    student for student in python_students if student[1] != lowest_score]


second_lowest_score_array = min(
    python_students, key=lambda student: student[1])

second_lowest_score = second_lowest_score_array[1]

student_names = [names[0]
                 for names in python_students if names[1] == second_lowest_score]


student_names.sort()

for name in student_names:
    print(name)
