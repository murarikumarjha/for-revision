try:
    print('try')
    print(10/0)
except ValueError :
    print('except')
finally:
    print('finally')
# if exception raised and not handled then abnormal termination will raised