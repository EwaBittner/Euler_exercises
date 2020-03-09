# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these \
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def main():

    my_list = list()

    number1 = 3
    number2 = 5

    for a in range(1000):
        if a % number1 == 0 or a % number2 == 0:
              my_list.append(a)

    multiplication_sum = sum(my_list)
    print("The list of number below 1000 that can be divided by 3 or 5: ", my_list)
    print()
    print("The sum of all these numbers is ", multiplication_sum)


main()
