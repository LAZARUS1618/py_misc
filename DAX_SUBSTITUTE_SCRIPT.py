# ETHAN GUECK
# This script is intended to assist in writing very repetitive DAX scripts

def RemoveLettersPrompt():
    response_Remove_Letters = input("Would you like to write a dax formula to remove all letters?\nType \"YES\" to see formula or \"NO\" to exit:  ")
    if response_Remove_Letters == "YES":
        return True
    elif response_Remove_Letters == "NO":
        return False
    else:
        print("Sorry try again:  ")
        return RemoveLettersPrompt()

def RemoveLetters(input_val):
    if input_val == True:
        z = ""
        for x in range(1, 27):
            y = chr(x + 96)  # convert number to lowercase letter
            b = chr(ord(y) - 1)
            a = f"var x_{y} = SUBSTITUTE(x_{b}, \"{y}\", \"\") return\n"
            z += a
        print(z)

#Remove letters Prompt


def RemoveSpacesPrompt():
    response_Remove_Letters = input("Would you like to write a dax formula to remove all Spaces and Dashes?\nType \"YES\" to see formula or \"NO\" to exit:  ")
    input_val = RemoveLettersPrompt()
    if response_Remove_Letters == "YES":
        return True
    elif response_Remove_Letters == "NO":
        return RemoveLetters(input_val)
    else:
        print("Sorry try again:  ")
        return RemoveSpacesPrompt()

def RemoveSpaces(input_val):
    if input_val == True:
        z = ""
        for x in range(2, 9, 2):
            c = x-1
            a = c-1
            a = f"var Base_Search_{c} = IF(LEFT(Base_Search_{a},1)=\"-\", RIGHT(Base_Search_{a},LEN(Base_Search_{a})-1), Base_Search_{a}) return\n"
            z += a
            a = f"var Base_Search_{x} = IF(LEFT(Base_Search_{c},1)=\" \", RIGHT(Base_Search_{c},LEN(Base_Search_{c})-1), Base_Search_{c}) return\n"
            z += a
        for x in range(10, 18, 2):
            c = x-1
            a = c-1
            a = f"var Base_Search_{c} = IF(RIGHT(Base_Search_{a},1)=\"-\", LEFT(Base_Search_{a},LEN(Base_Search_{a})-1), Base_Search_{a}) return\n"
            z += a
            a = f"var Base_Search_{x} = IF(RIGHT(Base_Search_{c},1)=\" \", LEFT(Base_Search_{c},LEN(Base_Search_{c})-1), Base_Search_{c}) return\n"
            z += a
        print(z)

#Remove letters Prompt
input_val = RemoveSpacesPrompt()
RemoveSpaces(input_val)
