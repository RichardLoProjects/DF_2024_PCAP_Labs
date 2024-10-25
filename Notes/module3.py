#raise ValueError('this file should not run')
obj_or_cls = None
_cls = None
obj = None
new_value = None
cls_name = None
cls_child = None
cls_parent = None





'''python class stuff'''
obj_or_cls.__dict__
hasattr(obj_or_cls, 'attr_name')
_cls.__name__
obj_or_cls.__module__
_cls.__bases__
getattr(obj, 'attr_name')
setattr(obj, 'attr_name', new_value)
isinstance(obj, cls_name)
str(obj) # via __str__(self)
issubclass(cls_child, cls_parent)

## class, obj, inheritance, private, __dict__, hasattr, property, method, constructor


class Classy:
    def visible(self):
        print("visible")
    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible() #visible
try:
    obj.__hidden() #error
except:
    print("failed") #failed
obj._Classy__hidden() #hidden


class ExampleObj:
    def __init__(self, value):
        self.v = value

x = ExampleObj(5)
y = x
## 3.5.1.6 objects are like lists. If x changes then so does y because they both point to same location in memory.
## 2.5.1.8 super() can be used for more than super().__init__()
## override hierachy:
##     1. inside itself
##     2. superclasses (bottom to top) and if multi-inheritance then (left to right)
##     3. AttributeError

## multi inheritance, overriding, polymorphism, inheritance vs composition, method-resolution-order


def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)
print_exception_tree(BaseException)











class AbstractClass:
    def __init__(self):
        if self.__class__ is AbstractClass:
            raise TypeError("Can't instantiate abstract class AbstractClass")

    def abstract_method(self):
        raise NotImplementedError("Abstract method 'abstract_method' must be implemented in subclasses")


class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("ConcreteClass implementing abstract_method")


# Example usage
try:
    abstract_instance = AbstractClass()  # This will raise an error since AbstractClass is abstract
except TypeError as e:
    print(e)

concrete_instance = ConcreteClass()
concrete_instance.abstract_method()  # This will print "ConcreteClass implementing abstract_method"



