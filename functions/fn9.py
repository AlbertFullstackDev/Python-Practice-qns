# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def check_prime_number(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not prime number.")


number = int(input("Insert a number to check if its prime number: "))
check_prime_number(number)
