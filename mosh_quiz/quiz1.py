# A program to display even numbers btn 1-10 without using step in range()
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
