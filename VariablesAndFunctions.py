# noinspection PyMethodParameters
class VariablesAndFunctions:

    # Example file for variables
    #

    # Declare a variable and initialize it

    f = 0

    print (f)

    # # re-declaring the variable works

    f = 123

    print(f)

    # # ERROR: variables of different types cannot be combined

    print("This is a string " + str(f))

    # Global vs. local variables in functions

    def someFunction():

        global f
        f = "This is the someFunction function"
        print(f)

    someFunction()
    print(f)

    del f

    #print (f)

    print("3! is " + str(1 * 2 * 3))