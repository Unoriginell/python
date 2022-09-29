from enum import Enum, auto


class Backend:
    class __State(Enum):
        # automatically assign rising numbers to enums starting from 1
        monday = auto()
        tuesday = auto()
        wednesday = auto()
        thursday = auto()
        friday = auto()
        saturday = auto()
        sunday = auto()

    def get_first_day_number(self):
        return self.__State.monday.value

    def get_last_day_number(self):
        return self.__State.sunday.value

    def interpret_command(self, command_index):
        if command_index == self.__State.monday.value:
            print("It is monday")
        elif command_index == self.__State.tuesday.value:
            print("It is tuesday")
        elif command_index == self.__State.wednesday.value:
            print("It is wednesday")
        elif command_index == self.__State.thursday.value:
            print("It is thursday")
        elif command_index == self.__State.friday.value:
            print("It is friday")
        elif command_index == self.__State.saturday.value:
            print("It is saturday")
        elif command_index == self.__State.sunday.value:
            print("It is sunday")


