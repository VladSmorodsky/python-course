def analyze_inheritance(class_name):
    """Function represents parent class methods
    :param class_name: Analyzed class
    """
    print(f"Class {class_name.__name__} extends:")
    for parent_class_item in class_name.__bases__:
        for item_name, item in vars(parent_class_item).items():
            if callable(item):
                print(f"- {item_name} from {parent_class_item.__name__}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
