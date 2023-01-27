from __future__ import annotations
import os
import requests
from trip import Trip

API_TOKEN = os.environ.get('API_TOKEN') 

def get_cheapest_flights(my_trip: Trip) -> None:
    params={
        "origin" : f"{my_trip.destination_from}",
        "destination" : f"{my_trip.destination_to}",
        "depart_date" : f"{my_trip.depart_date}",
        "return_date" : f"{my_trip.return_date}",
        "token" : f"{API_TOKEN}"
    }
    data = requests.get("http://api.travelpayouts.com/v1/prices/cheap",params)
    print(data.text)

dummy_trip = Trip("2023-02","2023-02","VAR","-")
get_cheapest_flights(dummy_trip)