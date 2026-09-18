from app import calculate_premium

def test_premium():
    assert calculate_premium(1000, 200) == 800
