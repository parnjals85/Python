# name = input("enter your name : ");

# # result = len(name);
# # result = name.find("p")
# result = name.rfind("p")
# print(result);

# UserName Not More than - 12 charcter's 

# name = input("Enter Username Name : ");

# if len(name) > 12:
#     print("Opps Seems Like Username is Exceed the Number Of Charcter")
# elif not name.find(" ") == -1:
#     print("Opps Not A Space needed");
# elif not name.isalpha():
#     print("Username Not Contain Any Digit Number");
# else:
#     print(f"Hello {name}")

# credit_card = '1234-56789-10111213'
# # [Start : end : step]
# credit_card = credit_card[::-1];
# print(credit_card)

email= input("Enter your Gmail");
username = email[:email.index("@")];
domain = email[email.index("@")+1];

print(f"Your Username is {username} and Domain is {domain}");