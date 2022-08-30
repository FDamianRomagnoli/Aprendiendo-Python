#v3.9 de python

from typing import Dict, List, Tuple

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '4500000'},
    {
        'name': 'Uruguay',
        'people': '100000'}
]

numbers: Tuple[int, float, int] = (1, 1.5, 2)

CoordinatesType = List[Dict[str, Tuple[int,int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,5)
    },
    {
        'coord1': (0,1),
        'coord2': (2,5)
    }
]