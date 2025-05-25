from adforward.dual import DualNumber


def test_dual_init():
    """Test the creation of a dual number"""
    x = DualNumber(1, 2)
    assert x.real == 1
    assert x.dual == 2


def test_dual_add():
    """Test the addition of two dual numbers"""
    a = DualNumber(1, 2)
    b = DualNumber(2, 1)
    c = a + b
    assert c.real == 3
    assert c.dual == 3


def test_dual_sub():
    """Test the substraction of two dual numbers"""
    a = DualNumber(1, 2)
    b = DualNumber(2, 1)
    c = a - b
    assert c.real == -1
    assert c.dual == 1


def test_dual_mul():
    """Test the multiplication of two dual numbers"""
    a = DualNumber(1, 2)
    b = DualNumber(2, 1)
    c = a * b
    assert c.real == 2
    assert c.dual == 5


def test_dual_div():
    """Test the division of two dual numbers"""
    a = DualNumber(1, 2)
    b = DualNumber(2, 1)
    c = a / b
    assert c.real == 0.5
    assert c.dual == 0.75
