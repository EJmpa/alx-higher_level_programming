def safe_print_list_integers(my_list=[], x=0):
  count = 0
    if(my_list):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                count += 1
            except IndexError:
                print()
                return(count)
    print()
    return(count)
