# Practice problems related exception handling and debugging 
# Problem 1
def safeDivision(a, b):
    try:
        divide = a / b
        return divide
    except:
        return "Can't divide by zero!"

print(safeDivision(2, 0))
print(safeDivision(12, 6))

# Problem 2
while True:
    try:
        num = int(input("Enter the valid integer: "))
        print("Thank You")
        break
    except ValueError:
        print("Invalid input! try again..!")


# Problem 3
try:
    with open("data.txt", "r") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Operation complete")


# Problem 4
def check_positive(num):
    if num < 0:
        raise ValueError("Number must be positive!")
    return num

print(check_positive(10))  
print(check_positive(-5))  


# Problem 5
try:
    text = input("Enter some text: ")
    with open("output.txt", "w") as file:
        file.write(text)
except IOError:
    print("Could not write to file!")
finally:
    print("Writing complete")


# Problem 6
try:
    with open("log.txt", "r") as f:
        r = f.read()
    with open("log.txt", "a") as f:
        f.write("New log entry\n")
except FileNotFoundError:
    print("File not found. Creating new file...")
    with open("log.txt", "w") as f:
        f.write("Log file created\n")
finally:
    print("Operation done")



# Problem 7:
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num  
        print(result)
    return result

print(multiply_list([1, 2, 3, 4]))


 #Problem 8   
try:
    num = int(input("Enter a number: "))
    divide = 100/num
    print(divide)
except ValueError:
  print("Not a number!")
except ZeroDivisionError:
  print("Cannot divide by zero!")

# Finding Second largest number
nums = [2, 5, 1, 5, 9, 4]
largest = 0
second = 0
for num in nums:
    if num > largest:
        largest, second = num, largest   # swaping
    elif num > second and num < largest:
        second = num
print("Second largest number:", second)

