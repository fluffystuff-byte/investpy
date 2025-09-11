# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

import investpy

def test_investpy_news():
    """
    This function checks that investpy news retrieval functionality works as expected.
    """

    params = [
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': ['spain', 'france'],
            'importances': ['high', 'low'],
            'categories': ['credit', 'employment'],
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': 'GMT -3:00',
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/02/2020'
        }
    ]

    for param in params:
        investpy.economic_calendar(time_zone=param['time_zone'],
                                   time_filter=param['time_filter'],
                                   countries=param['countries'],
                                   importances=param['importances'],
                                   categories=param['categories'],
                                   from_date=param['from_date'],
                                   to_date=param['to_date'])
