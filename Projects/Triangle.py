row = int(input("Enter the Number Of Rows : "));
column = int(input("Enter the Number of Column : "));
symbol = input("Enter the Symbol : ");

for x in range(row):
    for y in range(column):
        print(symbol ,end="");
    print();
