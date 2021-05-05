# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

student_scores = {'John': 45, 'Larry': 64, 'Jane': 56, 'Alexa': 87, 'Mosh': 25}

sorted_asc = sorted(student_scores.items(), key=lambda item: item[1])

sorted_desc = sorted(student_scores.items(),
                     key=lambda item: item[1], reverse=True)

print(f"Asc Order: {sorted_asc}")
print(f"Desc Order: {sorted_desc}")
