class ExDict(dict):
    def rm(self):
        tmp = []
        for key in self.keys():
            if self[key] == '':
                tmp.append(key)

        for key in tmp:
            del(self[key])
        del(tmp)

if __name__ == '__main__':
    d = {
        'a':1,
        'b':2,
        'c':'',
        'd':'d'
    }
    test = ExDict()
    test.update(d)
    print(test)
    test.rm()
    print(test)