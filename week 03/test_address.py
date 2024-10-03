# Teams Wk3  -- Wed 8PM MT
# Description - Test File for Teams assignment for addresses

from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the test_extract_city function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_city("10229 E Iron Horse Trl, Tucson, AZ 85747") == "Tucson"
    assert extract_city("1234 E Broadway Blvd, New York City, NY 10280") == "New York City"

def test_extract_state():
    """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_state("10229 E Iron Horse Trl, Tucson, AZ 85747") == "AZ"
    assert extract_state("1234 E Broadway Blvd, New York City, NY 10280") == "NY"

def test_extract_zipcode():
    """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_zipcode("10229 E Iron Horse Trl, Tucson, AZ 85747") == "85747"
    assert extract_zipcode("1234 E Broadway Blvd, New York City, NY 10280") == "10280"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
