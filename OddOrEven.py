# ODD OR EVEN

# fixes str in float/int
# fixes ValueError for letters instead of Numbers
# while/try/except/else
# if/elif

# Ask the user for a number.

while True:
    try:
        num_1 = (str(input("Pick a number.  ")))
        num_str = num_1.split(" ")[0]
        num_2 = int(float(num_str))
    except ValueError:
        print("\nERROR; please type a number!")
        continue
    else:
        break

remainder = num_2 % 2
while True:
    try:
        check_1 = (str(input("Pick a number to divide your previous number by.  ")))
        check_str = check_1.split(" ")[0]
        check_2 = int(float(check_str))
    except ValueError:
        print("\nERROR; please type a number!")
        continue
    else:
        break
print("\nYour Numbers:")
print(">Your number is {}.".format(num_2))
print(">The number to divide by is {}.".format(check_2))

print("\nAnswer:")

if num_2 % 4 == 0:
    print(">This number is a multiple of '4'.")
elif remainder == 0:
    print(">You picked an even number.")
elif remainder == 1:
    print(">You picked an odd number.")
if num_2 % check_2 == 0:
    print(">Your number is divisible by {}".format(check_2))
elif num_2 % check_2 != 0:
    print(">Your number is NOT divisible by {}".format(check_2))
#
#


# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# Discussion
