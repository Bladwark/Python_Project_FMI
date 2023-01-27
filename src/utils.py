"""
Module containg usefull functions for operating with the app
"""
from typing import Dict

def make_beautiful_response(data: Dict[str,str]) -> Dict[str,str]:
    """
    Recieves json object as python dict and extracts needed information
    """
    result = dict(key = "value")
    return result