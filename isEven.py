

def is_even(n):

    if (n % 1) == 0:
        if (n % 2) == 0:
            print("True")
            return True

        else:
            print("False")
            return False
    else:
        print(f"{n} is not an integer")



is_even(-4)