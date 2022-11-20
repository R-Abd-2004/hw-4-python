# # Second Question
# # -------------------

num1 = float(input("Enter Your Number: ").strip())

operation = input("""Enter Your Operation
    1_ +
    2_ -
    3_ *
    4_ /
    5_ ^
    6_ %
""").strip()

num2 = float(input("Enter Your Number: ").strip())

if operation == "+" or operation == "1":

    result =  num1 + num2

    print(f"The Answer Is: {num1} + {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

elif operation == "-" or operation == "2":

    result =  num1 - num2

    print(f"{num1} - {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

elif operation == "*" or operation == "3":

    result =  num1 * num2

    print(f"{num1} * {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

elif operation == "/" or operation == "4":

    result = num1/num2

    print(f"{num1} / {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

elif operation == "^" or operation == "5":

    result = num1**num2

    print(f"{num1} ^ {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

elif operation == "%" or operation == "6":

    result = num1%num2

    print(f"{num1} % {num2} = {result}")

    other_option = input("""Choose: 
    1_ "Round Up a Number"
    2_ "Take the number without a decimal point"
    3_ "Exit"
    """)

    if other_option == "1" :

        print(round(result))

    elif other_option == "2" :

        print(int(result))

    elif other_option == "3" :

        print("Exit")

    else:

        print("Thir are No Other Option")

else:

    print("Invalid Operation")

##########################################################################