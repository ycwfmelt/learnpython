# def choose_class(name):
#     if name=='foo':
#         class Foo(object):
#             pass
#         return Foo
#     else:
#         class Bar(object):
#             pass
#         return Bar

# MyClass = choose_class('foo')

# print(type(MyClass))
# print(type(MyClass()))

def upper_attr(future_class_name,future_class_parents,future_class_attr):
    """
        Return a class object,with the list of its attribute turned into uppercase        
    """