#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if x == 0:
                return 0
            else:
                print("{}".format(my_list[i]), end = "")
                count += 1
        print()
        return count
    except BaseException:
        print()
        return i
    print()

