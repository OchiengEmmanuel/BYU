
"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"




#def test_extract_family_name():
#    -----------------




#def test_extract_given_name():
 #   ---------------
    


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])