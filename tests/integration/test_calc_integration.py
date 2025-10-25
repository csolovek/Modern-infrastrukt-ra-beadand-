from src.calc import Calculator

def test_chain_operations():
    c = Calculator()
    # Simulate a small flow using multiple methods
    total = c.add(5, 7)        # 12
    result = c.divide(total, 3)  # 4
    assert result == 4

