try:
    x = int (input ('Enter the first Numerate: '))
    y = int (input ('Enter the second Numerate: '))
    result = (x / y) 
    print ('the result is ', result)
except ZeroDivisionError:
print("ZeroDivisionError : cannot divide with zero")
except:
    print ("Defult Except : please provide valid input only")
    #  Defult Except block should be last except block

# except ZeroDivisionError:
#     print("ZeroDivisionError : cannot divide with zero")