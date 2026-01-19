weight = float(input("Enter your Weight: "))
unit = input("Enter the Unit (K for Kilograms, L for Pounds): ").upper()

if unit == 'K':
    weight = weight * 2.205
    unit = "LBS"
elif unit == 'L':
    weight = weight / 2.205
    unit = "KGS"
else:
    print("Invalid unit entered")
    exit()
print(f"Your Weight is: {round(weight, 2)} {unit}")
