#!/usr/bin/env python3
""" google_api.py
"""
from googlemaps import Client


def geocode_address(address):
    """
    Geocode an address using Google Maps API.

    Args:
        address (str): The address to geocode.

    Returns:
        dict: Geocoding information.
    """
    gmaps = Client(key='AIzaSyCqoeDgkfk_2-3csLzYkPcu9JU5iOSN_Uk')
    geocoding_result = gmaps.geocode(address)

    if geocoding_result:
        return geocoding_result[0]['geometry']['location']
    else:
        return None
