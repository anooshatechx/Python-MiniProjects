#Math Toolkit
while True:
	menu = print("""What you want to do?:
a. Addition
b. Subtraction
c. Multiplication
d. Division
e. Square
f. Square Root
g. Exit""")
	print()
	user = input("Enter what you chose: ").strip().lower()
	if user in ["a","b","c","d"]:
		num1 = int(input("Enter 1 number: "))
		num2 = int(input("Enter 2 number: "))
	elif user in ["e","f"]:
		sq = int(input("Enter a number: "))
	if user == "a":
		print(f"Sum of {num1} and {num2} is: {num1 + num2}")
	elif user == "b":
		print(f"Subtract of {num1} and {num2} is {num1-num2}")
	elif user == "c":
		print(f"Mutiplication of {num1} and {num2} is {num1*num2}")
	elif user == "d":
		if num2 == 0:
			print("Denominator cannot be 0")
		else:
			print(f"Division of {num1} and {num2} is: {num1/num2}")
	elif user == "e":
		print(f"The square of {sq} is {sq**2}")
	elif user == "f":
		print(f"Square root of {sq} is {sq**0.5}")
	print()
	again = input("Do you want another calculation? y/n: ")
	if again.strip().lower() != "y":
		break
	print()
else:
	print("Invalid Input")
