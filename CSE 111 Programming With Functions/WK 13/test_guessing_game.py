from guessing_game import eo_generate_multiplication_problem, eo_check_multiplication_answer
import pytest

def test_eo_generate_multiplication_problem():
    # Generate multiple multiplication problems and confirm if the numbers are within the specified range
    for _ in range(100):
        num1, num2 = eo_generate_multiplication_problem()
        assert 1 <= num1 <= 20
        assert 1 <= num2 <= 20

def test_eo_check_multiplication_answer():
    # Test case 1: Correct answer
    num1, num2 = 12, 19
    guess = num1 * num2
    assert eo_check_multiplication_answer(num1, num2, guess) == True

    # Test case 2: Incorrect answer
    num1, num2 = 8, 4
    
    # This is for the Incorrect answer
    guess = 10 
    assert eo_check_multiplication_answer(num1, num2, guess) == False


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])