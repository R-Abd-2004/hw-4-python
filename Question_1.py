# First question
# -------------------

name = input("Enter Your Name: ")

if name == '' or name.isspace() == True:

    print("Wrong Name")

else:

    age = int(input("Enter Your Age: "))    

    address = input("Enter Your Address: ")

    if address == '' or address.isspace() == True:
        print("Wrong Address")

    else:
        print(f"Hello Mr/Ms {name.strip()} Age {age} Located in {address}. Thanks For Beening One Of Our Community,   Enjoy")

#########################################################################