
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if num % 2 == 0:
        print("true")
        return True
    else:
        print("false")
        return False

is_even(num)


user_input = int(input("Now, enter a different number: "))

def is_it_even(user_input):
    if user_input % 2 == 0:
        print("Even!")
    else:
        print("Odd")
# Print out "Even!" if the number is even. Otherwise print "Odd"

is_it_even(user_input)

