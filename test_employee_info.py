import employee_info as info

def test_get_employees_by_age_range():
    result = info.get_employees_by_age_range(20, 30)
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert (result == test)

def test_calculate_average_salary():
    result = info.calculate_average_salary()
    test = (50000+60000+56000+70000+65000+60000)/6
    assert (result == round(test,2))

def test_get_employees_by_dept():
    result = info.get_employees_by_dept("Marketing")
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert (result == test)