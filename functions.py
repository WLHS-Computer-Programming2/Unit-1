import math

def my_function(num_times:int) -> None:
    """This function will print the
    phrase "Hello" num_times times

    Parameter
    ---------
    int: num_times

    Return
    ------
    None
    """
    print("Hello!"*num_times)


def multiple_checker(number:int, factor:int)->bool:
    """This function determines if a number is
    a factor of another number
    
    Parameters
    ----------
    number:int - number I want to check
    factor:int - factor to check

    Return
    ------
    boolean - true if factor is a factor of number,
              false if not
    """
    if number % factor == 0:
        return True
    else:
        return False

# write a function called length_comparison
# that takes in two string arguments and 
# tells the user which string is longer
# and returns the length of the longest string

def length_comparison(string1:str, string2:str)->int:
    """The functions tells a user which of two strings
    is longer and returns that length"""
    try:
        if len(string1)>len(string2):
            print(f"{string1} is longer than {string2}")
            return len(string1)
        elif len(string1) < len(string2):
            print(f"{string2} is longer than {string1}")
            return len(string2)
        else:
            print("They are the same length!")
            return len(string2)
    except TypeError:
        print("Enter string values only")

def square_root_fun(number:int)->float:
    try:
        if not str(number).isdigit():
            raise ValueError
        return math.sqrt(number)/number
    except ValueError:
        print("Number must be a positive integer")
    except ZeroDivisionError:
        print("Number must be a positive integer")

print(square_root_fun(100.4))
    
# while True:
#     try:
#         word_one = input("Enter a word: ")
#         word_two = input("Enter a word: ")
#         if word_one.isdigit() or word_two.isdigit():
#             raise TypeError
#         length_comparison(word_one,word_two)
#     except TypeError:
#         print("Enter strings only")
