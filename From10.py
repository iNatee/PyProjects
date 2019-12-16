class UserInput:

    def operateTo10(userOp, userNum):

        if userOp == "+":
            return 10 + userNum

        elif userOp == "-":

            if userNum < 10:
                return 10 - userNum

            else:
                return userNum - 10

    goAgain = "Yes"
    while goAgain == "Yes":
        userOp = raw_input("Which operation to do to 10?\n")
        userIn = raw_input("Which number do you want to " + str(userOp) + " 10?\n")
        userNum = int(userIn)
        print("10 " + str(userOp) + " " + str(userNum) + " = " + str(operateTo10(userOp, userNum)))
        goAgain = raw_input("Do you want to do the from 10 game?\n")

    print("Goodbye and have a good day :)")
