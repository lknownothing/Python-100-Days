'''
和类属性一样，类方法也可以进行更细致的划分，具体可分为类classmethod, instancemethod, staticmethod。函数装饰器@staticmethod的为静态方法；不用任何修改的方为instancemethod。
ref:http://c.biancheng.net/view/4552.html
'''
# instancemethod # 常规self
class Language():
    # 最大的特点是至少要包含self参数，用于绑定调用此方法的实例对象
    def __init__(self):
        self.name="C语言"
        self.web="https://www.cplusplus.com/"

    def say(self):
        print("正在调用instance方法")

C=Language()
C.say()

# classmethod 不用呆着self, 而是使用cls
'''
类方法和实例方法类似，至少要包含一个参数，类方法通常将其命名为cls。python会自动将类本身绑定给cls参数(注意，绑定的不是类对象)。也就是说，调用类方法时，无需显示为cls参数传递。
'''
class Pad():
    def __init__(self):
        self.name="Ipad"
        self.price="￥3399"
    
    @classmethod
    def info(cls):
        print("正在调用class方法",cls)

# 推荐使用类名直接调用
Pad.info()

# staticmethod 静态方法直接使用参数
'''
静态方法，其实就是我们学过的函数，唯一的区别是，静态方法定义在类这个空间（类命名空间），而函数定义在全局命名空间。没有类似self, cls这样的参数，python解释器不会对它包含的参数做任何类或对象的绑定。类的静态方法中无法调用任何类属性和类方法。
'''
class Food():
    @staticmethod
    def info(name,types):
        print("Food:",name,types)

Food.info("白菜","蔬菜")


# all in one
class Bird():
    def __init__(self,name,sing):
        self.name=name
        self.sing=sing
    
    def fullinfo(self):
        print(f"{self.name}喜欢唱{self.sing}!")

    @classmethod
    def fly(cls):
        print("classmethod",cls)
    
    @staticmethod
    def info(food):
        print(f"小鸟喜欢吃{food}")

Bird.fly()
Bird.info("虫子")
B=Bird("鹦鹉","茉莉花")
B.fullinfo()