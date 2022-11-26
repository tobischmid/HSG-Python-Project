# This is a sample Python script.

print("This program will filter a list of words according to a length you specify")


def filter_my_words(string, number):
    listwords = []

    for i in range(len(string)):
        if len(string[i]) > number:
            listwords.append(string[i])
    return listwords


def main():
    words = input("Please input the list of words: ").split()
    integer = int(input("Please input an integer: "))

    filtered_words = filter_my_words(words, integer)

    print("The list of words greater than the integer is " + str(filtered_words))


main()