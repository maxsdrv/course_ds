

def get_total(units, price):
    return units * price


def sort_sides(l_in):

    return sorted(l_in, key=lambda x: (x[0]**2 + x[1]**2) ** (1/2)) 


def my_func(*args, **kwargs):
    print(args, kwargs)


# Base Course Python: Advanced using functions
#Recurtion

def sum_lst(lst):
    print(lst)

    if len(lst) == 0:return 0

    return lst[0] + sum_lst(lst[1:])

def multiply_lst(lst):
    if len(lst) == 0: return 1 

    return lst[0] * multiply_lst(lst[1:])

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    a1 = fib(n - 1)
    a2 = fib(n - 2)
    return a1 + a2

def power(val, n):
    if n == 0: return 1
    elif n == 1:
        return val
    elif n < 0:
        return 1 / power(val, -n)
    elif n % 2 == 0:
        return power(val * val, n // 2)
    else:
        return val * power(val * val, n // 2)

def is_leap(year):
    if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0: return True
    else: return False

# Эта функция работает следующим образом:
# Если хотя бы один из аргументов day, month или year не является целым числом, то возвращаем False.
# Если год рождения меньше 1900 или больше 2022, то возвращаем False.
# Если номер месяца меньше 1 или больше 12, то возвращаем False.
# Если месяц является апрелем, июнем, сентябрем или ноябрем, и номер дня меньше 1 или больше 30, то возвращаем False.
# Если месяц является февралем, год является високосным, и номер дня меньше 1 или больше 29, то возвращаем False.
# Если месяц является февралем, год не является високосным, и номер дня меньше 1 или больше 28, то возвращаем False.
# Если номер дня меньше 1 или больше 31, то возвращаем False.
# Если ни одно из вышеперечисленных условий не выполняется, то возвращаем True.
def check_date(day, month, year):
    if not (type(day) is int and type(month) is int and type(year) is int):
        return False
    if year < 1900 or year > 2022:
        return False
    if month < 1 or month > 12:
        return False
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    if month == 2 and is_leap(year) and (day < 1 or day > 29):
        return False
    if month == 2 and not is_leap(year) and (day < 1 or day > 28):
        return False
    if day < 1 or day > 31:
        return False
    return True

def register(surname, name, date, middle_name = None, registry = None):
    if registry is None: registry = []
    if not check_date(date[0], date[1], date[2]):
        raise ValueError("Invalid Date!")
    registry.append((surname, name, middle_name, date[0], date[1], date[2]))
    return registry


if __name__ == "__main__":
    print("Advanced Functions")

    reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
    reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
    reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
    print(reg)