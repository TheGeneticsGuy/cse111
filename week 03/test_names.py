# Author:       Aaron Topping
# Teams Wk3
# Description - Test File for Teams assignment

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("", "") == "; "
    assert make_full_name("ABC", "DEF") == "DEF; ABC"
    assert make_full_name("", "Smith") == "Smith; "
    assert make_full_name("Aaron", "Joseph-Topping") == "Joseph-Topping; Aaron"

def test_extract_family_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("") == ""
    assert extract_family_name("; ") == ""
    assert extract_family_name("; John") == ""
    assert extract_family_name("DEF; ABC") == "DEF"
    assert extract_family_name("Smith-Topping; ") == "Smith-Topping"
    assert extract_family_name("Topping; Aaron") == "Topping"

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_given_name("") == ""
    assert extract_given_name("; ") == ""
    assert extract_given_name("; John") == "John"
    assert extract_given_name("DEF; ABC") == "ABC"
    assert extract_given_name("Smith; ") == ""
    assert extract_given_name("Chu; Christine") == "Christine"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
