#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_counts = 0
    for i in range(x):
        try:
<<<<<<< HEAD
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except(ValueError, TypeError):
            pass
=======
            print("{:d}".format(my_list[i]), end="")
            int_counts += 1
        except (ValueError, TypeError):
            continue
>>>>>>> 19f90e2a61246af1464359dbab7678099c06d0f4
    print()
    return int_counts
