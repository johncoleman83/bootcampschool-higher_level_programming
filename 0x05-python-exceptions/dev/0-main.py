#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]
a = []
b = ['hi', 'there', 'how', 'are', 'you']
c = [my_list, a, b]
d = [(5, 3, 6), 66, "string"]
e = [(1, 2), (4, 5)]
f = [5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(a, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(b, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(c, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(d, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(e, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(f, 2)
print("nb_print: {:d}".format(nb_print))
