# 5. Write a Python program to count the number of strings where the string length is 2 or more
#  and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def check_strings(strings):
    count = 0
    for string in strings:
        if len(string) > 2 and string[0] == string[-1]:
            count += 1
    return count


strings = ['abc', 'xyz', 'aba', '1221']
print(f'The count is: {check_strings(strings)}')
