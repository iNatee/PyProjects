class PracticeFunctions:

    def addTo10(self):
        return 10 + self

    def addTo20(self):

        return 20 + self

    print("10/20 + what?")
    userIn = input()
    userInt = int(userIn)
    print("10 + " + str(userInt) + " = " + str(addTo10(userInt)))
    print("20 + " + str(userInt) + " = " + str(addTo20(userInt)))
