try :
    print(10/0)
except  BaseException as x :
    print('this s is exception on except')
    print('the type of exception ', type(x))
    print('the type of exception :', x.__class__)
    print('The exception name: ',x.__class__.__name__)
    print('The description of exception :',x)