class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print(x)

MyClass.the_static_method(2)  # outputs 2


class MyClass2(object):
    def the_static_method(x):
        print(x)
    the_static_method = staticmethod(the_static_method)

MyClass2.the_static_method(2)  # outputs 2

#https://stackoverflow.com/questions/735975/static-methods-in-python
#