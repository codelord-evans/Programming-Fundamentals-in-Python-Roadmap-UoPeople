# EXAMPLE 1 ==> This code example demonstrates the use Chained Contitionals to check whether a user is of the right age to access a website.
#age = int(input("What is you age?: "))
#if age >= 18: # Here goes the first contitional statement "if". If the user is 18 or older, they are allowed to access the website
#    print("Access granted")
#elif age < 13: # Here goes the second contitional statement "elif". If the user is younger than 13, they are not allowed to access the website
#    print("Access denied")
#else: # Here goes the third contitional statement "else". If the user is younger than 18 but older than 13, they are allowed to access the website
#    print("come back when you are older")


# EXAMPLE 2 ==> The code below demonstrates the use of nested conditionals to check whether a user is of the right age to access a website.
# This code checks if a user is of the right age before accessing a website
age = int(input("What is your age?: "))
if age >= 18:
    print("Access granted")
else:
    print("Access denied")
    consent = input("Do you have a consent from parent? (yes/no) ")
    if consent == "yes":
        print("Please enter the code sent to your parent's email")
        code = input("Enter the code: ")
        if code == "1234":
            print("Code accepted. Access granted")
        else:
            print("The code is incorrect")
    else:
        print("You need parental consent to access the website")


 # Strategies

def process_data(data):
    if not data:
        return "No data provided"

    if len(data) < 5:
        return "Not enough data"

    # Rest of the code
    return "Data processed successfully"
       
