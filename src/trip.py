"""
Module containing Trip class
"""

class Trip:
    """
    Contains all needed information about a trip
    """

    def __init__(self, depart_date: str, return_date: str, destination_from: str, destination_to: str, currency: str = "EUR") -> None:
        self.__depart_date = depart_date
        self.__return_date = return_date
        self.__destination_from = destination_from
        self.__destination_to = destination_to
        self.__curency = currency

    @property
    def depart_date(self) -> str:
        """ returns departure date """
        return self.__depart_date

    @depart_date.setter
    def depart_date(self, value: str) -> None:
        """ sets departure date """
        self.__depart_date = value

    @property
    def return_date(self) -> str:
        """ returns return date """
        return self.__return_date

    @return_date.setter
    def return_date(self, value: str) -> None:
        """ sets return date """
        self.__return_date = value

    @property
    def destination_from(self) -> str:
        """ returns destination from """
        return self.__destination_from

    @destination_from.setter
    def destination_from(self, value: str) -> None:
        """ sets destination from """
        self.__destination_from = value
    
    @property
    def destination_to(self) -> str:
        """ returns destination from """
        return self.__destination_to


    @destination_to.setter
    def destination_to(self, value: str) -> None:
        """ sets destination from """
        self.__destination_to = value

    @property
    def currency(self) -> str:
        """ returns currency """
        return self.__curency

    @currency.setter
    def currency(self, value: str) -> None:
        """ sets currency """
        self.__curency = value  
