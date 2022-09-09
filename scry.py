"""
Module for Scryfall API



Author: Laurence Lo
Date: Jul 12 2022
"""

import requests
import json
from time import sleep


#import sys
#droppedFile = sys.argv[1]
#print droppedFile


def get_all(name):
    """
    Returns a list of all printings of card name.

    parameter: (str) name of a card (case-insensitve)
    Precondition: exact name of existing MtG card (ONE WORD)
    """
    q = 'https://api.scryfall.com/cards/search?unique=prints&order=usd&q='
    q += name
    response = requests.get(q)
    sleep(.1)
    for data in response.json()['data']:
        if data['prices']['usd'] is not None:
            if data['name'] == name:
                print(data['name']+ ': ' + data['prices']['usd'] + '[' + data['set'] + ']')
    return response


def get_params(name):
    """
    Returns a list of all printings of card name.

    parameter: (str) name of a card (case-insensitve)
    Precondition: exact name of existing MtG card
    """
    load  = {
        'unique': 'prints',
        'order': 'usd',
        'dir': 'asc',
        'q': name
    }
    response = requests.get('https://api.scryfall.com/cards/search/', params=load)
    sleep(.1)
    for data in response.json()['data']:
        if data['prices']['usd'] is not None:
            if data['name'] == name:
                print(data['name']+ ': ' + data['prices']['usd'] + '[' + data['set'] + ']')
    return response


def get_cheapest(name):
    """
    Returns a cheapest of all printings of card name.

    parameter: (str) name of a card (case-insensitve)
    Precondition: exact name of existing MtG card
    """
    load  = {
        'unique': 'prints',
        'order': 'usd',
        'dir': 'asc',
        'q': name
    }
    response = requests.get('https://api.scryfall.com/cards/search/', params=load)
    sleep(.1)
    for data in response.json()['data']:
        if data['prices']['usd'] is not None:
            if data['name'] == name:
                #print(data['name']+ ' ' + data['prices']['usd'] + '[' + data['set'] + ']')
                price = data['prices']['usd']
                set = data['set'].upper()
                return price, set
    return response
