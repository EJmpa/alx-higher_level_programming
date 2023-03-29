def safe_print_division(a, b):
  try:
    return a / b
   except ZeroDivisionError:
    return None
   finally:
      print("{}".format(a / b))
    
