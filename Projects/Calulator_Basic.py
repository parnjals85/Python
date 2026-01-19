Ope = input("Enter the Operator")
a = int(input("Enter the Number A : "));
b = int(input("Enter the Number B : "));

if Ope == "+":
   print(f"Addtion of the Value {a} and {b} Is : ", a+b);
elif Ope == "-":
   print(f"Subtraction of the Value {a} and {b} is : " , a-b);
elif Ope == "*":
   print(f"Multiplication of the Value {a} and {b} is : " , a*b);
elif Ope == "/":
   print(f"Dividation of the {a} and {b} is : " , a/b);
elif Ope == "":
   print("Please Enter the Operator For Operation");
