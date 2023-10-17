from task import *

def test_calculator():

    calculator = Calculator()

    # Test addition
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

    # Test subtraction
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(10, 20) == -10

    # Test multiplication
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(-2, 3) == -6

    print("All test cases passed.")