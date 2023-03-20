

def get_total(units, price):
    return units * price


print(get_total(15, 50))



def sort_sides(l_in):

    return sorted(l_in, key=lambda x: (x[0]**2 + x[1]**2) ** (1/2)) 



print(sort_sides([(3, 4), (1, 2), (10, 10)]))


def my_func(*args, **kwargs):
    print(args, kwargs)



my_func(1, 5, {1: 5}, monday="python")