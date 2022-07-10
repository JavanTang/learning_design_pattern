from filecmp import cmp


class Car():
    """
    汽车类
    """
    def __init__(self, name) -> None:
        """
        初始化汽车类
        """
        self.name = name
    
    def __del__(self) -> None:
        """
        析构函数
        """
        print("汽车类已销毁")
    
    def __str__(self) -> str:
        """
        返回汽车类的字符串表示
        """
        return self.name
    
    def __repr__(self) -> str:
        return 'name: ' + self.name



car = Car('BMW')
print(car.__doc__)

# print
print(car)

# 销毁car, 虽然方法中仅仅是输出了一句话, 但是该对象的内存已经被销毁了
print('-----------------')

try:
    del car
    print(car)
except Exception as e:
    print('报错了')
    print(e)
print('-----------------')


car = Car('BMW')
print(repr(car))
print(str(car))


# 最后都会输出一个"汽车类已销毁",这应该是程序运行结束后会将这些对象销毁吧