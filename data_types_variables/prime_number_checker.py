number = int(input())
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if not is_prime:
    print("False")

elif is_prime or number ==2 or number == 3:
    print("True")
