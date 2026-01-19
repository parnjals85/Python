Tem = float(input("Enter the Temperature : "));
User = input("Please Enter the Temperature In Fareheight Or Celsius (F/Y) : ").upper();

if User == "F":
   c = (Tem * 9/5) + 32
   print(f"Farenheight Of the {Tem} is : {c} " );
elif User == "C":
    F = (Tem-32)* 5/9
    print(f"Celsius Of the {Tem} is : {F} ");
elif User == "":
   print("Please Enter the Valid Number")
