#Question 1
name = "Bhumika Agrawal"
age = 20
student_status = True
print(type(name))
print(type(age))
print(type(student_status))

#Question 2
a = 10
b = 20
a = a+b
b = a-b
a = a-b
c = "10"
print("After swapping: a =", a, "b =", b)   
print(type(a))
a=float(a)
print(type(a))
a=int(a)
print(type(a))
print(type(c))
c = int(c)
print(type(c))


#Question 3
name1 = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
branch = input("Enter your branch: ")  
marks = []

for i in range(5):
    marks.append(float(input("Enter marks of subject " + str(i + 1) + ": ")))

print(marks)
total_marks = 0
for j in marks:
    total_marks += j
print("Total marks:", total_marks)
average_marks = total_marks / len(marks)
print("Average marks:", average_marks)  
percentage = (total_marks / 500) * 100
print("Percentage:", percentage, "%")   

#Question 4
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
sub_total = product_price * quantity
print("Sub-total:", sub_total)
gst = sub_total * 0.18
print("GST (18%):", gst)    
final_total = sub_total + gst
print("Final bill is:", final_total)  


#Question 5
account_holder_name = input("Enter the account holder's name: ")
account_number = input("Enter the account number: ")
current_balance = float(input("Enter the current balance: "))
deposit_amount = float(input("Enter the deposit amount: "))
current_balance += deposit_amount
print("Updated balance after deposit:", current_balance)        
print(type(account_holder_name), type(account_number), type(current_balance), type(deposit_amount))

#PYTHON INPUT AND OUTPUT

#Question 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
mobile_number = input("Enter your mobile number: ")
print(f"Name: {name}, Age: {age}, City: {city}, Mobile Number: {mobile_number}")

#Question 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Modulus: ",a%b)


#Question 4
temprature_celsius = float(input("Enter temperature in Celsius: "))
temprature_fahrenheit = (temprature_celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {temprature_fahrenheit}, Temperature in Celsius: {temprature_celsius}")


#Question 5
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
sub_total = product_price * quantity
print("Sub-total:", sub_total)
gst = sub_total * 0.18
print("GST (18%):", gst)    
final_total = sub_total + gst
print("Final bill is:", final_total)  
