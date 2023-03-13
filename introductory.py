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

def hw1():
    str_nums = "100, 50, 55, 2, 3, 1, h, 9, pi, 400, ds, 4039"
    prepare_list = str_nums.split(" ")
    res_list = []
    for i in prepare_list:
        try:
            int(i)
            res_list.append(int(i))
        except ValueError:
            pass 
        else:
         res_list.sort()
         print(*res_list, sep=", ")






def real_round(args):
    count_digit = len(args[0]) - 1
    numb = eval(args[0].replace(",", ".")) 
    digit = eval(args[1])
    print(count_digit)

    
def lower_round(args):
    args[0] = args[0].replace(",", ".")
    return round(float(args[0]), int(args[1]))

def upper_round(args):
    args[0] = args[0].replace(",", ".")
    return round(float(args[0]), int(args[1]))

if __name__ == '__main__':
    print("test")

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

# str_input = input("Python helper")
str_input = "ОКРУГЛ(2.15;1)"
res_str = ""

it_begin = str_input.find("(") #iterator of begin list arguments
it_end = str_input.find(")") #iterator of end list arguments
if it_begin==-1 or it_end==-1:
    print("Error, function is not correct\n"
          "Please visit Excel https://...")

res_str = str_input[it_begin+1:it_end] # slice string for correct list function arguments

arg_list = res_str.split(";") 
print(arg_list[0], arg_list[1])

func_str = str_input[:str_input.find("(")] #for function name then we call it
print(func_str.lower())

result = 0

if func_str == "ОКРУГЛ":
    result = real_round(arg_list)
elif func_str == "ОКРУГЛВНИЗ":
    result = lower_round(arg_list)
else:
    result = upper_round(arg_list)

print("Python helper is monster: ", result)
print(round(3.2, 0))