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


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
        Return a class object,with the list of its attribute turned into uppercase        
    """
    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name,val in future_class_attr.items():
        if not name.startwith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
    return type(future_class_name,future_class_parents,uppercase_attr)

__metaclass__ = upper_attr  # this will affect all classes in the module

class Foo():
    