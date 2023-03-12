import shlex
import sys
import numpy


def test_lesson1():
    str = "maxim, egor, inga"
    names = str.split()
    maxim = names[0]
    inga = names[1]
    egor = names[2]
    
    print(f"We are {maxim} the {inga} champions {egor}")
    
    name = 'John'
    dayofweek = 'Friday'
    
    print("Hello {}! Today is {}. Have a nice day!.".format(name, dayofweek))



class Helper:
    def __init__(self):
        self._func = None

def from_str_to_int(str):
    number_int = 0
    
    if str.startswith('-'):
        str = str[1:]

        for index, char in enumerate(str):
            number_int += (ord(char) - ord("0")) * 10 ** (len(str) - 1 - index)
    
        number_int = number_int * (-1)
    else:
        for index, char in enumerate(str):
            number_int += (ord(char) - ord("0")) * 10 ** (len(str) - 1 - index)


    return number_int


if __name__ == '__main__':
    print("test");

number_str = "6"
dir(number_str)
number_str.__len__()
number_str.__eq__("6")
(1).__str__(), str(1)
ord("a"), ord("b") #ASCII compare
chr(97), chr(98)
ord(number_str) - ord("0")

#####################################
task_str = "61032"
print(from_str_to_int("-59"))

######################################







