class Proxy:
    """Class shows log message when original class method is called"""

    def __init__(self, obj: object) -> None:
        self.obj = obj

    def __getattr__(self, item: callable) -> callable:
        def log(*args, **kwargs):
            print(f"Method {item} was called with args: {args}")
            return getattr(obj, item)(*args, **kwargs)

        return log


class MyClass:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
