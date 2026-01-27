marks = []

while True:
    print("1. Add Marks")
    print("2. Show Marks")
    print("3. Highest Marks")
    print("4. Lowest Marks")
    print("5. Average Marks")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    # Add Marks
    if choice == 1:
        Add = int(input("Enter the Student Marks : "))
        marks.append(Add)
        print("Marks added Successfully")

    # Show Marks
    elif choice == 2:
        if not marks:
            print("No marks available")
        else:
            print("Marks List:")
            for m in marks:
                print(m)

    # Highest Marks
    elif choice == 3:
        if not marks:
            print("No marks available")
        else:
            print("Highest Marks :", max(marks))

    # Lowest Marks
    elif choice == 4:
        if not marks:
            print("No marks available")
        else:
            print("Lowest Marks :", min(marks))

    # Average Marks
    elif choice == 5:
        if not marks:
            print("No marks available")
        else:
            avg = sum(marks) / len(marks)
            print("Average Marks :", avg)

    # Exit
    elif choice == 6:
        print("Exit Program Bye!!")
        break

    else:
        print("Invalid Choice")
