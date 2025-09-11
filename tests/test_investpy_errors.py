# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

import investpy

def test_news_errors():
    """
    This function raises errors on news functions.
    """

    params = [
        {
            'time_zone': ['error'],
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': 'error',
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': None,
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': ['error'],
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': 'error',
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': 'error',
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': 'error',
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': ['error'],
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': ['error']
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/02/2020'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': 'error',
            'to_date': '01/02/2020'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': 'error'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/01/2019'
        }
    ]

    for param in params:
        try:
            investpy.economic_calendar(time_zone=param['time_zone'],
                                  time_filter=param['time_filter'],
                                  countries=param['countries'],
                                  importances=param['importances'],
                                  categories=param['categories'],
                                  from_date=param['from_date'],
                                  to_date=param['to_date'])
        except:
            pass