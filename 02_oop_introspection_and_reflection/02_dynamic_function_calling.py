def call_function(obj, method_name: str, *args) -> str:
    """
    Function calls automatically object's (obj) method (method_name) with arguments (args)
    :param obj:
    :param method_name:
    :param args:
    :return str:
    """
    if not hasattr(obj, method_name):
        return f"Object {obj} has no attribute {method_name}"
    if not callable(getattr(obj, method_name)):
        return f"Object {obj} has no method {method_name}"

    try:
        return getattr(obj, method_name)(*args)
    except TypeError as error:
        return error.__str__()


class Calculator:
    c = 1

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()

print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
