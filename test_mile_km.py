import pytest
def miles_to_km(miles):
    return miles * 1.60934
def test_miles_to_km():
    assert round(miles_to_km(5), 2) == 8.05
    assert round(miles_to_km(1), 2) == 1.61
    assert round(miles_to_km(0), 2) == 0.00