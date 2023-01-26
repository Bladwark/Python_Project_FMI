""" Representation of a Trip class that contains all the data needed for flight search """

class Trip:

    def __init__(self, depart_date: str, return_date: str, destination_from: str, destination_to, currency: str = "EUR") -> None:
        pass

    @property
    def depart_date(self) -> str:
        """ returns departure date """
        return ""

    @depart_date.setter
    def depart_date(self, value: str) -> None:
        """ sets departure date """
        pass

    @property
    def return_date(self) -> str:
        """ returns return date """
        return ""

    @return_date.setter
    def return_date(self, value: str) -> None:
        """ sets return date """
        pass

    @property
    def destination_from(self) -> str:
        """ returns destination from """
        return ""

    @destination_from.setter
    def destination_from(self, value: str) -> None:
        """ sets destination from """
        pass
    
    @property
    def destination_to(self) -> str:
        """ returns destination from """
        return ""

    @destination_to.setter
    def destination_to(self, value: str) -> None:
        """ sets destination from """
        pass

    @property
    def currency(self) -> str:
        """ returns currency """
        return ""

    @currency.setter
    def currency(self, value: str) -> None:
        """ sets currency """
        pass
