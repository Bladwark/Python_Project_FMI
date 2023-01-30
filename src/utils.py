"""
Module containg usefull functions for operating with the app
"""
# from __future__ import annotations
from typing import Dict, List
# for future me: get time from return and arival and calcuclate it to 
# local time at the city u start your trip from

def modify_response_date(date: str) -> str:
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
            flight["departure_at"] = modify_response_date(flight["departure_at"])
            flight["return_at"] = modify_response_date(flight["return_at"])
            flight["expires_at"] = modify_response_date(flight["expires_at"])
            city_dict = dict(city_from = city_from,city_to = city)
            temp_result = f"{city_dict['city_from']}-{city_dict['city_to']} | from {flight['departure_at']} to {flight['return_at']} | avaliable until {flight['expires_at']} | {flight['price']} EUR"
            # result.append(temp_result)
            result.append(dict(city_dict, **flight))

    result.sort(key = (lambda el: el["price"]))
    answer = map ((lambda x: f"{x['city_from']}-{x['city_to']} | from {x['departure_at']} to {x['return_at']} | avaliable until {x['expires_at']} | {x['price']} EUR" ), result)
    
    return list(answer)
