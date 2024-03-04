from BMI App import calculate_bmi, classify

def test_calculate_bmi():
    assert calculate_bmi(160, 5, 8) == pytest.approx(24.34, 0.01)

def test_classify_underweight():
    assert classify(18.0) == "You are Underweight"

def test_classify_normal_weight():
    assert classify(22.0) == "You are Normal Weight"

def test_classify_overweight():
    assert classify(27.0) == "You are Overweight"

def test_classify_obese():
    assert classify(35.0) == "You are Obese"
