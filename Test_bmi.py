from  Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    assert calculate_bmi(40, 1.53) == -1

def test_bmi_over_weight():
    result = calculate_bmi(88, 1.73)
    assert  (result == 1)

def test_bmi_normal_weight():
    result = calculate_bmi(57, 1.73)
    assert  (result == 0)
