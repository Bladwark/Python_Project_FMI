"""
Module containg functionality that this app supports
"""

from __future__ import annotations
import os
import requests
from typing import Dict
from trip import Trip
from utils import make_beautiful_response
import json

API_TOKEN = os.environ.get('API_TOKEN') 

# we asume trip input here will be always correct
def get_cheapest_flights(my_trip: Trip) -> None | Dict[str, Dict[str, Dict[str,str]]]:
    """
    Makes request to API and returns flights coresponding to given parameters
    """
    params={
        "origin" : f"{my_trip.destination_from}",
        "destination" : f"{my_trip.destination_to}",
        "depart_date" : f"{my_trip.depart_date}",
        "return_date" : f"{my_trip.return_date}",
        "token" : f"{API_TOKEN}",
        "currency" : f"{my_trip.currency}"
    }
    data = requests.get("http://api.travelpayouts.com/v1/prices/cheap",params)
    if data.status_code == 200:
        pretty_data = json.loads(data.text)
        return pretty_data['data']

    return None

if __name__ == "__main__":
    dummy_trip = Trip("2023-02","2023-02","SOF","-")
    flights = get_cheapest_flights(dummy_trip)
    if flights != None:
        list = make_beautiful_response(dummy_trip.destination_from,flights)
        for el in list:
            print(el)
        
    