#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This is a programs that finds the sign of a integer


def main():
    user_input = input("Enter a integer: ")
    # Cast user input to a integer
    user_num = int(user_input)
    # Check the numbers and display the output
    if user_num > 0:
        print("The number {} is positive.".format(user_num))
    elif user_num == 0:
        print("The number {} is neutral.".format(user_num))
    else:
        print("The number {} is negative".format(user_num))


if __name__ == "__main__":
    main()
