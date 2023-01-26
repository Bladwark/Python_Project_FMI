"""
Module containing the unittests for the Trip class
"""

import pytest
from src.trip import Trip

def test_001_create_instance():
    """
    Verify that properties are set correctly
    """
    #Arrange
    dummy_depart_date = "01-01-2020"
    dummy_return_date = "01-02-2020"
    dummy_destination_from = "SOF"
    dummy_destination_to = "IST"
    dummy_currency = "BGN"

    #act
    has_raised_exception = False
    try:
        trip = Trip(dummy_depart_date,dummy_return_date,dummy_destination_from,dummy_destination_to,dummy_currency)
    except Exception:
        has_raised_exception = True

    #assert
    assert not has_raised_exception
    assert isinstance(trip, Trip)