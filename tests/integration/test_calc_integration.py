from src.calc import Calculator

def test_flow():
    c = Calculator()
    total = c.add(1, 2)
    total = c.add(total, 3)
    assert total == 6
