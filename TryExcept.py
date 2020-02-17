from pip._vendor.distlib.compat import raw_input


class TryExceptTest:
    try:
        print("Test Case 1. This will fail due to concatenation failure" + 1)

    except:
        print("Exception caught")

    finally:
        print("Program ended")