# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_upper_lower_characters(string):
    count_upper = 0
    count_lower = 0

    for character in string:
        if (character.isupper()) == True:
            count_upper += 1
        elif(character.islower()) == True:
            count_lower += 1
    print(f"No. of Upper case characters : {count_upper}")
    print(f"No. of Lower case characters : {count_lower}")


count_upper_lower_characters('The quick Brow Fox')
