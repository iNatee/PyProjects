class UserInput:

    def doMinusOrPlus(userOp, userNum, userNum2):

        if userOp == "+":
            return str(str(userNum) + " + " + str(userNum2) + " = " + str(userNum + userNum2))

        elif userOp == "-":

            print("Would you like to do?" + "\n" + "1. " + str(str(userNum) + str(userOp) + str(userNum2)) + "\n" + "2. " + str(str(userNum2)  + str(userOp) + str(userNum)) + "?")
            userSum = input()
            userSum = int(userSum)
            validIn = 1

            while validIn == 1:

                validIn = 1

                if userSum == 1:
                    return str(str(userNum) + str(userOp) + str(userNum2) + " = " + str(userNum - userNum2))
                elif userSum == 2:
                    return str(str(userNum2) + str(userOp) + str(userNum) + " = " + str(userNum2 - userNum))
                else:
                    validIn = 0
                    return "Invalid input. Try again"

    goAgain = "Yes"
    while goAgain == "Yes":
        userOp = raw_input("Which operation to do to\n")
        userNum = input("Which numbers do you want to " + str(userOp) + "\nNum 1: ")
        userNum = int(userNum)
        userNum2 = input("Num 2: ")
        userNum2 = int(userNum2)
        print(str(doMinusOrPlus(userOp, userNum, userNum2)))
        goAgain = raw_input("Do you want to do the from 10 game?\n")

    print("Goodbye. The program has now ended. Have a good day")
