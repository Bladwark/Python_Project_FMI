"""
Module containg usefull functions for operating with the app
"""
from __future__ import annotations
from typing import Dict, List
from trip import Trip
from functionality import get_cheapest_flights
# for future me: get time from return and arival and calcuclate it to 
# local time at the city u start your trip from

def _modify_response_date(date: str) -> str:
    """
    Removes time stamp from returned date of flight
    """
    return date.split("T")[0]

# def make_beautiful_response(city_from: str ,data: Dict[str, Dict[str, Dict[str,str]]]) -> List[Dict[str,str]]:
def make_beautiful_response(city_from: str ,data: Dict[str, Dict[str, Dict[str,str]]]) -> List[str]:
    """
    Recieves json object as python dict and extracts needed information
    """
    result: List[Dict[str,str]] = []
    for city, flights in data.items():
        for flight in flights.values():
            flight["departure_at"] = _modify_response_date(flight["departure_at"])
            flight["return_at"] = _modify_response_date(flight["return_at"])
            flight["expires_at"] = _modify_response_date(flight["expires_at"])
            city_dict = dict(city_from = city_from,city_to = city)
            # temp_result = f"{city_dict['city_from']}-{city_dict['city_to']} | from {flight['departure_at']} to {flight['return_at']} | avaliable until {flight['expires_at']} | {flight['price']} EUR"
            # result.append(temp_result)
            result.append(dict(city_dict, **flight))

    result.sort(key = (lambda el: el["price"]))
    answer = map ((lambda x: f"{x['city_from']}-{x['city_to']} | from {x['departure_at']} to {x['return_at']} | avaliable until {x['expires_at']} | {x['price']} EUR" ), result)
    
    return list(answer)

def get_tickets(depart_date: str, return_date: str, destination_from: str, destination_to: str, currency: str) -> List[str] | None:
    """
    Returns list of tickets by givent trip data
    """
    if currency != "-":
        my_trip = Trip (depart_date, return_date, destination_from, destination_to, currency)
    my_trip = Trip (depart_date, return_date, destination_from, destination_to)
    flights = get_cheapest_flights(my_trip)
    
    #TODO: if flights is Empty == no such tickets, waht to do
    if not flights:
        return []
    #TODO: if API response is not valid, waht to do 
    if flights is None:
        return None
    
    return make_beautiful_response(my_trip.destination_from ,flights)

def is_valid_date(date: str) -> bool:
    return True

def is_valid_city(date: str) -> bool:
    return True