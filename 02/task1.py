def analyze_object(obj: object) -> None:
    """
    Function represents analysed object's info
    :param obj:
    :return:
    """

    def get_object_members(analysed_obj: object) -> str:
        """
        Function returns analysed object's members info
        :param analysed_obj:
        :return:
        """
        object_members_info = ""

        object_members = dir(analysed_obj)
        for object_member_name in object_members:
            if object_member_name.startswith('__'):
                continue
            object_members_info += f"- {object_member_name} {type(getattr(analysed_obj, object_member_name))}\n"

        return object_members_info

    print(f"Object type: {type(obj)}\n"
          f"Attributes and methods:\n"
          f"{get_object_members(obj)}")


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


my_class = MyClass('test')
analyze_object(my_class)
