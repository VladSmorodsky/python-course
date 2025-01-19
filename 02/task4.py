def create_class(class_name: str, method_list):
    """
    Function for creating dynamic class using class_name string and method_list methods
    :param class_name:
    :param method_list:
    :return:
    """
    return type(class_name, (), method_list)


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
