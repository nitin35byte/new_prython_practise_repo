#1. Using try-except for Error Handling
try:
    num= int(input("enter a number"))
    result= 1/num
    """
    How it Works:
    The try block contains the code that may raise an exception.
    The except blocks handle specific errors (ZeroDivisionError, ValueError).
    A generic except Exception as e catches any unexpected errors.
    """

    print("result:" ,result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



#2. Using finally for Cleanup
try:
    file=open("test.txt",'r')
    content=file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found.")
    """
    Use Case:
    Closing files, database connections, or releasing resources regardless of success or failure.
    """
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("file closed")


#3. Using else with try-except
#The else block runs only if no exceptions occur in the try block.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

    """
    🔹 Use Case:
    Separating normal execution (else) from error handling (except).
    """
else:
    print("Success! Result is:", result)

#4. Raising Custom Exceptions
#You can raise exceptions using the raise keyword.

def validate_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    return "Access granted."
"""
🔹 Use Case:
Enforcing business rules (custom error messages).
Preventing incorrect data from being processed.
"""
try:
    print(validate_age(15))
except ValueError as e:
    print("Validation Error:", e)

#5. Creating Custom Exception Classes
#For more control, define your own exception class.
class CustomError(Exception):
    """Custom exception for specific errors."""
    pass
    """🔹 Use Case:
    Making error handling more structured in large applications.
    
    """
try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print("Caught Custom Exception:", e)


#6. Logging Exceptions (Best Practice)
#Instead of just printing errors, use the logging module for better tracking.
import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    x = 10 / 0

    """
       🔹 Use Case:
       Keeping error records for debugging in production environments.
       """
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)
    print("An error was logged.")

# 7. Handling Multiple Exceptions in One Line
# You can catch multiple exceptions in a single except block.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)

# 8. Exception Handling in Loops
# If an error occurs inside a loop, you can continue execution.

numbers = [10, 0, 5]

for num in numbers:
    try:
        print("Result:", 10 / num)
    except ZeroDivisionError:
        print("Skipping division by zero.")



# 🚀 Summary of Best Practices
# ✅ Always handle exceptions explicitly.
# ✅ Use finally for cleanup (closing files, releasing resources).
# ✅ Use else when needed to separate error-free execution.
# ✅ Log errors instead of just printing them.
# ✅ Raise custom exceptions for better error messages.