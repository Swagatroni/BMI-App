import pytest
from bmi_app import calculate_bmi, classify

def test_calculate_bmi():
    assert calculate_bmi(160, 5, 8) == pytest.approx(24.9, 0.01)
    assert calculate_bmi(675, 7, 9) == pytest.approx(56.2, 0.01)

def test_bad_inputs():
    with pytest.raises(ValueError, match = "Invalid input values"):
        assert calculate_bmi(100, 6, 15)
        assert calculate_bmi(-120, 4, 6)
        assert calculate_bmi(0, 0, 0)
        assert calculate_bmi("a", "b", "c")


def test_classify_underweight():
    assert classify(4.5) == "You are Underweight"
    assert classify(10.48) == "You are Underweight"
    assert classify(16.61) == "You are Underweight"
    assert classify(18.49) == "You are Underweight"

def test_classify_normal_weight():
    assert classify(18.5) == "You have a Normal Weight"
    assert classify(20.46) == "You have a Normal Weight"
    assert classify(23.667) == "You have a Normal Weight"
    assert classify(24.9) == "You have a Normal Weight"

def test_classify_overweight():
    assert classify(25.0) == "You are Overweight"
    assert classify(26.243) == "You are Overweight"
    assert classify(28.15) == "You are Overweight"
    assert classify(29.9) == "You are Overweight"

def test_classify_obese():
    assert classify(30.0) == "You are Obese"
    assert classify(38.183) == "You are Obese"
    assert classify(53.15) == "You are Obese"
    assert classify(453.2) == "You are Obese"

def test_classify_valErr():
    with pytest.raises(ValueError, match = "Invalid BMI value"):
        assert classify(-0.0)
        assert classify(-38.183)
        assert classify(123)

def test_classify_typeErr():
    with pytest.raises(TypeError, match = "'<=' not supported between instances of 'int' and 'str'" ):
         assert classify("test")
