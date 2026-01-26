# 1. Temperature Converter
# 2. Weight Converter
# 3. Email Analyzer
# 4. Weather Condition Checker
# 5. Daily Health Tip
# 6. Exit

# tem = float(input("Enter the Temperature : "));


# check = input("Please Verify You needed In Farheight or in Kelvin (F/K): ");

# if check == "F":
#     f = (tem * 9/5) + 32
#     print(f"Farheight is the Temperature {tem}: ", f);
# elif check == "K":
#     k =  tem + 273.15;
#     print(f"Kelvin is the Temperature {tem} : " , k);
# elif check == "":
#     print("Please enter the Any value");

#user chnage KG - Gram  and 
#user chnage Gram - KG 

# weight = float(input("Please Enter the Weight : "));

# check = input("Please Verify the Weight you enter in Kg or Gram (K/G): ");

# if check == "K":
#   k = weight * 1000;
#   print(f"Weight in the KG is the  ", k);
# elif check == "G":
#     g = weight / 1000;
#     print(f"Weight in the Gram is the ", g);
# elif check == "":
#    print("Sorry! you not enter the Any Value");

# email = input("Enter Your Email: ");
# if "@" in email and "." in email:
#     username = email[:email.index("@")]
#     domain = email[email.index("@") + 1:]

#     print("Username:", username)
#     print("Domain:", domain)

#     if domain == "gmail.com":
#         print("Provider: Gmail");
#     elif domain == "yahoo.com":
#         print("Provider: Yahoo")
#     elif domain == "Outlook.com":
#         print("Provider: Outlook")
#     else:
#         print("Provider: Other")

# else:
#     print("Invalid Email Address");

# Wheather Checker -

# checker = float(input("Enter the Temperature : "))
# if 1 <= checker <= 20:
#     print("Good! Weather Condition Is Cool")
# elif 21 <= checker <= 50:
#     print("There is a Sunny Day Outside")
# else:
#     print("Opps Sorry Please enter the Valid Temperature")

# Daily Health Tip
# user print 1 - show something , click 2 - something like 

Health = float(input("Enter the health level (1 to 5): "));
if Health == 1:
    print("Very Poor Health");
elif Health == 2:
    print("Poor Health");
elif Health == 3:
    print("Average Health")
elif Health == 4:
    print("Good Health")
elif Health == 5:
    print("Excellent Health")
else:
    print("Invalid! Number Your Put");











