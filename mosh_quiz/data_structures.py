# Find the character with most occurences in sentence
sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char_frequency = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
print(sorted_char_frequency[0])
