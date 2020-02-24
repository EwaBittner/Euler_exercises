# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these \
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def main():

    my_list3 = []
    my_list5 = []

    number1 = 3
    number2 = 5

    for a in range(1000):
        result = a * number1
        my_list3.append(result)
        a += 1

    multiplication_sum_3 = sum(my_list3)

    print("The sum of all multiples of 3 below 1000 is ", multiplication_sum_3)
    print(my_list3)
    print()

    for b in range(1000):
        result = b * number2
        my_list5.append(result)
        b += 1

    multiplication_sum_5 = sum(my_list5)

    print("The sum of all multiples of 3 below 1000 is ", multiplication_sum_5)
    print(my_list5)


main()
