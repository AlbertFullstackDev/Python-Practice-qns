# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n, print i^2.
n = int(input('input:'))

if 1 <= n <= 20:
    for i in range(n):
        print(f'{i**2}')
else:
    print("Please enter a number btn 1-20")
