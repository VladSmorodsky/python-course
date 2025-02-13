import inspect


def get_functions_info(function_name: str, function_object: callable) -> str:
    """
    Function returns into about function object
    :param function_name:
    :param function_object:
    :return str:
    """
    function_arguments_info = ''
    function_arguments = inspect.getfullargspec(function_object).args

    for arg in function_arguments:
        function_arguments_info += arg
        if function_arguments.index(arg) != len(function_arguments) - 1:
            function_arguments_info += ', '

    return f"{function_name}({function_arguments_info})\n"


def analyze_module(module_name: str) -> None:
    """
    Function shows functions and classes in the module
    :param module_name:
    :return None:
    """
    import importlib
    module = importlib.import_module(module_name)

    module_members = inspect.getmembers(module)

    module_functions_info = 'Functions:\n'
    module_classes_info = 'Classes:\n'

    for module_member in module_members:
        # Skip magic methods
        module_member_name = module_member[0]
        module_member_obj = module_member[1]

        if module_member_name.startswith('__'):
            continue

        if inspect.isclass(module_member_obj):
            module_classes_info += f'{module_member_name}\n'
            continue

        if callable(module_member_obj):
            try:
                module_functions_info += get_functions_info(module_member_name, module_member_obj)
            except TypeError:
                continue

    print(f"{module_functions_info}\n{module_classes_info}")


analyze_module("math")
