# noinspection PyMethodParameters
class PracticeFunctions:

    def addTo10(userIn):
        return 10 + userIn

    def addTo20():

        return 20

    print("10/20 + what?")
    userIn = input()
    userInt = int(userIn)
    print("10 + " + str(userInt) + " = " + str(addTo10(userInt)))
    print("20 + " + str(userInt) + " = " + str(addTo20() + userInt))
