def log_methods(class_name):
    """Decorator function that adds logging info for class's methods execution

    :param class_name: class name for decorating
    """
    def method_logger(cls_method_name, cls_method):
        """Function for adding log info and executing class method"""
        def log(*args, **kwargs):
            print(f'Logging: {cls_method_name} called with {args[1:]}')
            return cls_method(*args, **kwargs)

        return log

    for attribute_name, value in vars(class_name).items():
        if callable(value):
            setattr(class_name, attribute_name, method_logger(attribute_name, value))

    return class_name


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)