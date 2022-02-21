import random 

#Introduction, Global Variables, Main Function
name = input("What is your name?: ")
print("")
print("Welcome to the calculator, " + name)
global variable1, variable2, answer, redo
def calculator():

#function input

    print("")
    function = input("What would you like this calculator to do:\n\n1:Add\n\n2:Subtract\n\n3:Multiply\n\n4:Divide\n\n5:Square(^2)\n\n6:Square Root\n\n7:Cube(^3)\n\n: ")


#addition
    if function.lower() == "1":
        def add():
            global variable1
            print("")
            variable1 = input("Enter First number: ")

            global variable2
            variable2 = input("Enter Another Number: ")

            global answer
            answer = int(variable1) + int(variable2)

            print("")
            print(variable1, "+", variable2, "=", answer)

            global redo
            print("")
            redo = input("Would you like to use the calculator once more?:\nYes\nNo\n: ")

        add()

#Subtraction
    if function.lower() == "2":
        def substract():
          global variable1
          print("")  
          variable1 = input("Enter First number: ")

          global variable2
          variable2 = input("Enter Another number: ")

          global answer
          answer = int(variable1) - int(variable2)

          print("")
          print(variable1, "-", variable2, "=", answer)

          global redo
          print("")
          redo = input("Would you like to use the calculator once more:\nYes\nNo\n: ")

        substract()

#Multiplication
    if function.lower() == "3":
        def Multiple():
          global variable1
          print("")  
          variable1 = input("Enter First Number: ")

          global variable2
          variable2 = input("Enter Another Number: ")

          global answer
          answer = int(variable1) * int(variable2)

          print("")
          print(variable1, "*", variable2, "=", answer)

          global redo 
          print("")
          redo = input("Would you like to use the calculator once more\nYes\nNo\n: ")
        Multiple()

#Division
    if function.lower() == "4":
      def divide():
        global variable1
        print("")  
        variable1 = input("Enter First Number: ")

        global variable2 
        variable2 = input("Enter Another Number: ")

        global answer
        answer = int(variable1) / int(variable2)

        print("")
        print(variable1, "/", variable2, "=", answer)

        global redo 
        print("")
        redo = input("Would you like to use the calculator once more\nYes\nNo\n: ")
      divide()

# Square 
    if function.lower() == "5":
      def square():
        global variable1
        print("")  
        variable1 = input("Enter First Number: ")

        global answer
        answer = int(variable1) * int(variable1)

        print("")
        print(variable1,"^2", "=", answer)

        global redo 
        print("")
        redo = input("Would you like to use the calculator once more\nYes\nNo\n:")
      square()

#Square Root
    if function.lower() == "6":
        def root():
          global variable1
          print("")      
          variable1 = input("Enter First Number: ")

          global answer
          answer = int(variable1) ** 0.5 

          print("")
          print(variable1, "square root =", answer)

          print("")
          global redo
          redo = input("Would you like to use the calculator once more\nYes\nNo\n:")
        root()

#Cube
    if function.lower() == "7":
        def cube():
          global variable1
          print("")  
          variable1 = input("Enter First Number: ")

          global answer
          answer = int(variable1) * int(variable1) * int(variable1)
          print("")

          print(variable1, "Cubed =", answer)
          print("")

          global redo
          redo = input("Would you like to use the calculator once more\nYes\nNo\n:")
        cube()    






calculator()


#reset
while redo.lower() == "y":
    calculator()
while redo.lower() == "yes":
      calculator()

#If no
if redo.lower() == "n":
    print("Thanks for using the calculator, " + name, "!")
if redo.lower() == "no":
  print("Thanks for using the calculator, " + name,"!")
