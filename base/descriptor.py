class RevealAccess:
    """一个数据描述符，正常设定值并返回值，同时打印出访问的信息
    """

    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Updating", self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, "var 'x'")
    y = 5
