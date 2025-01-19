class MutableClass:
    def add_attribute(self, name: str, value) -> None:
        """Set new attribute"""
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """Remove attribute"""
        delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений
