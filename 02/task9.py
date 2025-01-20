class DynamicProperties:
    def add_property(self, name: str, default_value):
        """Function creates property with name and default_value value.
        Also, it is responsible for creating property name getter and setter"""

        def get_property(prop_name: str):
            return self.__dict__[name]

        def set_property(prop_name: str, value) -> None:
            self.__dict__[prop_name] = value

        setattr(self, name, property(get_property, set_property))

        if default_value is not None:
            setattr(self, name, default_value)


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
