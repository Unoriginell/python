from backend import Backend


class MyGUI:
    def __init__(self):
        __backend_object = Backend()
        first_day_index = __backend_object.get_first_day_number()
        last_day_index = __backend_object.get_last_day_number()
        for x in range(first_day_index, last_day_index + 1):
            __backend_object.interpret_command(x)
