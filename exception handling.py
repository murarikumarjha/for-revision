try :
    X = int(input('ENTER FIRST NUMBER '))
    Y = int(input('ENTER SECOND NUMBER '))
    print('the reult :', X/Y)
except  BaseException as  msg :
    print('the type of exception :', type(msg))
    print('the type of exception :', msg.__class__)
    print('the name of exception',msg.__class__.__name__)