print("YOU CAN NOW DO YOU SIMPLE MATH RIGHT HERE...:")
oparetor = ("+ * - / ")
operation = float(input("Enter first number :"))
symbol = oparetor = input("ENTER symbol :")
operation2 = float(input("Enter second number :"))
# print out the results
if symbol == "+":
    print(operation + operation2)
elif symbol == "-":
    print(operation - operation2)
elif symbol == "*":
    print(operation * operation2)
elif symbol == "/":
    print(operation / operation2)
else:
    print("invalid option")
