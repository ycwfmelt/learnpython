class Folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self, nesting=0):
        offset = " " * nesting
        print("{}{}/".format(offset, self.name))

        for element in self:
            if hasattr(element, "dir"):
                element.dir(nesting + 1)
            else:
                print("{} {}".format(offset, element))

if __name__ == '__main__':
    tree = Folder("project")
    tree.append('README.md')
    tree.dir()
    src = Folder("src")
    src.append("script.py")
    tree.append(src)
    tree.dir()