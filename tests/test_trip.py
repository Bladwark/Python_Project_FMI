"""
Module containing the unittests for the Trip class
"""

import pytest
from src.trip import Trip

def create_dummy_instance() -> Trip:
    """
    creates dummy instance of a trip object
    """
    dummy_depart_date = "01-01-2020"
    dummy_return_date = "01-02-2020"
    dummy_destination_from = "SOF"
    dummy_destination_to = "IST"
    dummy_currency = "BGN"

    return Trip(dummy_depart_date,dummy_return_date,dummy_destination_from,dummy_destination_to,dummy_currency)


def test_001_create_instance() -> None:
    """
    Verify that properties are set correctly
    """
    #Arrange
    dummy_depart_date = "01-01-2020"
    dummy_return_date = "01-02-2020"
    dummy_destination_from = "SOF"
    dummy_destination_to = "IST"
    dummy_currency = "BGN"

    #Act
    has_raised_exception = False
    try:
        trip = Trip(dummy_depart_date,dummy_return_date,dummy_destination_from,dummy_destination_to,dummy_currency)
    except Exception:
        has_raised_exception = True

    #Assert
    assert not has_raised_exception
    assert isinstance(trip, Trip)

def test_002_get_Trip_object_properties() -> None:
    """
    Verifies that all of getters are working correct
    """
    #arrange
    dummy_trip = create_dummy_instance()
    dummy_depart_date = "01-01-2020"
    dummy_return_date = "01-02-2020"
    dummy_destination_from = "SOF"
    dummy_destination_to = "IST"
    dummy_currency = "BGN"

    #Act
    dummy_depart_date_returned = dummy_trip.depart_date
    dummy_return_date_returned = dummy_trip.return_date
    dummy_destination_from_returned = dummy_trip.destination_from
    dummy_destination_to_returned = dummy_trip.destination_to
    dummy_currency_returned = dummy_trip.currency

    #Assert
    assert dummy_depart_date == dummy_depart_date_returned
    assert dummy_return_date == dummy_return_date_returned
    assert dummy_destination_from == dummy_destination_from_returned
    assert dummy_destination_to == dummy_destination_to_returned
    assert dummy_currency == dummy_currency_returned

def test_003_get_Trip_object_properties() -> None:
    """
    Verifies that all data is being set correctly
    """
    #Arrange
    dummy_trip = create_dummy_instance()

    #Act
    dummy_trip.depart_date = "02-02-2018"
    dummy_trip.return_date = "02-03-2018"
    dummy_trip.destination_from = "MSK"
    dummy_trip.destination_to = "NYC"
    dummy_trip.currency = "USD"

    #Assert
    assert dummy_trip.depart_date == "02-02-2018"
    assert dummy_trip.return_date == "02-03-2018"
    assert dummy_trip.destination_from == "MSK"
    assert dummy_trip.destination_to == "NYC"
    assert dummy_trip.currency == "USD"
