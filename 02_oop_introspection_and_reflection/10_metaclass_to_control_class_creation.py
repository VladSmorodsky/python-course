class SingletonMeta(type):
    """Class is responsible for creating and storing single class instances."""
    __instances = {}

    def __call__(cls, *args, **kwargs):
        """Function is responsible for creating single cls instance and returning it when it exists."""
        if cls not in cls.__instances:
            new_instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = new_instance
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True
