
class test:
    def __init__(self,foo):
        self._foo=foo

    def _bar(self):
        print(self._foo)
        print("可以访问函数__bar(), 函数_bar()也可以访问私有")

def main():
    test1=test("hello")
    test1._bar() # test1 have no object name attribute _Bar
    print("访问下划线私有：",test1._foo)
    test1._foo="Hello world!"
    print("也可以更改：", test1._foo)

if __name__=="__main__":
    main()