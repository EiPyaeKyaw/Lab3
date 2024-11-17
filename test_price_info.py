import price_info as info
info.price_list = {"apple":1, "grape":3}
info.quantity_list = {"apple":4, "grape":5}
def test_total_cost_shopping():
    result = info.total_cost_shopping()
    test = 19
    assert (result == test)

def test_cost_of_fruits():
    result = info.cost_of_fruits('apple',3)
    test = 3
    assert (result == test)