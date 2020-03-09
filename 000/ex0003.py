# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def prime_factor():
    prime_numbers = list()

    tested_number = int(input("Write the number you want to test: "))
    if tested_number % 2 == 0:
        even_nmbr = tested_number / 2
        prime_numbers.append(even_nmbr)
    else:
        if tested_number % 3 == 0:
            odd_nmbr = tested_number / 3
            prime_numbers.append(odd_nmbr)

    print("The number is: ", prime_numbers)


prime_factor()
