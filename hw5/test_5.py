from unittest.mock import patch
import urllib.request
import json
from issue5 import what_is_year_now
import pytest

def test_year1():
    exp_year = 2021

    with patch.object(urllib.request, 'urlopen'):
        with patch.object(json, 'load', return_value={'currentDateTime': '2021-03-20'}):
            actual_year = what_is_year_now()

    assert exp_year == actual_year


def test_year2():
    exp_year = 2019

    with patch.object(urllib.request, 'urlopen'):
        with patch.object(json, 'load', return_value={'currentDateTime': '01.03.2019'}):
            actual_year = what_is_year_now()

    assert exp_year == actual_year


def test_exc():
    exp_year = 2019

    with patch.object(urllib.request, 'urlopen'):
        with patch.object(json, 'load', return_value={'currentDateTime': '01 03 2019'}):
            with pytest.raises(ValueError):
                actual_year = what_is_year_now()

