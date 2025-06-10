# We are going to take Arithmatic mean of n-numbers
from sympy import sympify

# We are first getting an universal function to check for integer numbers
from is_definitely_Real import is_definitely_real
from Is_definitely_Integer import is_definitely_integer

# First start with taking inputs from the user
n = "Hey_Its_Naval"
total = 0 


while is_definitely_integer(n) == False:

    try: 
        n = int(input("Enter the number of numbers you have to take arithmatic mean of: "))
    except ValueError:
        print("Value error: You have not entered an INTEGER, Please try again!!")
    except Exception as e:
        print(f"Error: {e}, Please try again!!")

numbers = {}

# Now we are getting every number in a dictionary named "numbers" so we can access them easily and they are also separated by a key & value
for number in range (1, n+1):

    numbers[f"n{number}"] = "Hey_Its_Naval"

    # defining the suffixes for some numbers

    if (str(number) == "1"):
        suffix = "st"
    elif (str(number) == "2"):
        suffix = "nd"
    elif (str(number) == "3"):
        suffix = "rd"
    else:
        suffix = "th"   

    while is_definitely_real(numbers[f"n{number}"]) == False:
        try: 
            numbers[f"n{number}"] = float(input(f"Enter the {number}{suffix} number: "))
        except ValueError as ve:
            print(f"You have not entered an real number. Please try again!!")
        except Exception as e:
            print(f"Error: {e}")

# Now, We will add all the numbers

else: 
    for number in range(1, n+1):
        temp = f"n{number}"
        total += numbers[temp]

# And finally we get our arithmatic mean

Arithmatic_Mean = total/n   

print(f"The Arithmatic Mean of the numbers is: {Arithmatic_Mean}")

