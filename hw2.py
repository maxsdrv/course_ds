




def parser(a_str):
    res_str = ""
    it_begin = a_str.find("(") #iterator of begin list arguments
    it_end = a_str.find(")") #iterator of end list arguments
    if it_begin==-1 or it_end==-1:
        print("Error, function is not correct\n"
              "Please visit Excel https://...")
    res_str = a_str[it_begin+1:it_end] # slice string for correct list function arguments
    arg_list = res_str.split(";") 
    arg_list[0] = arg_list[0].replace(",", ".")

    func_name = a_str[:a_str.find("(")] #for function name then we call it

    number = eval(arg_list[0]) # first function arg
    digit = eval(arg_list[1]) # second function arg

    if func_name == "ОКРУГЛ":
        result = round_rel(number, digit)
    elif func_name == "ОКРУГЛВНИЗ":
        result = round_down(number, digit)
    elif func_name == "ОКРУГЛВВЕРХ":
        result = round_up(number, digit)
    else:
       raise ValueError("Name function doesn't exist")

    return result



def round_rel(number, num_digits):
    factor = 10 ** num_digits
    rounded = round(number * factor)

    return rounded / factor

def round_up(number, num_digits):
    factor = 10 ** num_digits

    s = str(number)
    if s.startswith("-"):
        number = (-number)
        rounded = -(-number * factor // 1)
        return (-rounded) / factor 

    rounded = -(-number * factor // 1)

    return rounded / factor

def round_down(number, num_digits):
    factor = 10 ** num_digits

    s = str(number)
    if s.startswith("-"):
        rounded = -number * factor // 1
        return (-rounded) / factor

    else:
        rounded = number * factor // 1
        return rounded / factor

def TEST(l1, l2):
    count_err = 0
    count_tests = 0
    for index, req in enumerate(l1):
        if parser(req) != eval(l2[index]):
            count_err += 1
            print(parser(req))
            print(l2[index])
        else:
            count_tests += 1

    if count_err == 0:
        print("ALL ", count_tests, "TESTS SUCCESSFULLY")
    else:
        print("TEST FINISHED with", count_err, "Errors")

###################################################################
###################################################################

if __name__ == '__main__':
    print("HW 2")


#TESTS:

# Round down
test_lst_down = [
    "ОКРУГЛВНИЗ(3,2; 0)",
    "ОКРУГЛВНИЗ(76,9;0)",
    "ОКРУГЛВНИЗ(3,14159; 3)",
    "ОКРУГЛВНИЗ(-3,14159; 1)",
    "ОКРУГЛВНИЗ(31415,92654; -2)"
]

answ_lst_down = [
    "3.0",
    "76.0",
    "3.141",
    "-3.1",
    "31400.0"    
]
print("Start Test excel_ROUNDDOWN")
TEST(test_lst_down, answ_lst_down)

#Round up
test_lst_up = [
    "ОКРУГЛВВЕРХ(3,2;0)",
    "ОКРУГЛВВЕРХ(76,9;0)",
    "ОКРУГЛВВЕРХ(3,14159; 3)",
    "ОКРУГЛВВЕРХ(-3,14159; 1)",
    "ОКРУГЛВВЕРХ(31415,92654; -2)",
]
answ_lst_up = [
    "4",
    "77",
    "3.142",
    "-3.2",
    "31500.0"
]
print("Start Test excel_ROUNDUP")
TEST(test_lst_up, answ_lst_up)


#Round real
test_lst_real = [
    "ОКРУГЛ(2,15; 1)",
    "ОКРУГЛ(2,149; 1)",
	"ОКРУГЛ(-1,475; 2)",
    "ОКРУГЛ(21.5; -1)",
    "ОКРУГЛ(626,3;-3)",
    "ОКРУГЛ(1,98;-1)",
    "ОКРУГЛ(-50,55;-2)",
]
answ_lst_real = [
    "2.2",
    "2.1",
    "-1.48",
    "20",
    "1000",
    "0",
    "-100"
]

print("Start Test excel_ROUND")
TEST(test_lst_real, answ_lst_real)















