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


def test_dual_pow():
    """Test raising a dual number to the power of 3"""
    a = DualNumber(2, 1)
    b = a**3
    assert b.real == 8
    assert b.dual == 12


def test_dual_eq():
    """Test equality comparison"""
    a = DualNumber(5, 2)
    b = DualNumber(5, 3)
    c = DualNumber(3, 2)

    assert a == b
    assert not (a == c)
    assert a == 5
    assert not (a == 3)


def test_dual_ne():
    """Test inequality comparison"""
    a = DualNumber(5, 2)
    b = DualNumber(3, 2)

    assert a != b
    assert a != 3
    assert not (a != 5)


def test_dual_lt():
    """Test less than comparison"""
    a = DualNumber(3, 2)
    b = DualNumber(5, 1)

    assert a < b
    assert a < 5
    assert not (b < a)
    assert not (a < 3)


def test_dual_le():
    """Test less than or equal comparison"""
    a = DualNumber(3, 2)
    b = DualNumber(5, 1)
    c = DualNumber(3, 5)

    assert a <= b
    assert a <= c
    assert a <= 5
    assert a <= 3
    assert not (b <= a)


def test_dual_gt():
    """Test greater than comparison"""
    a = DualNumber(5, 2)
    b = DualNumber(3, 1)

    assert a > b
    assert a > 3
    assert not (b > a)
    assert not (a > 5)


def test_dual_ge():
    """Test greater than or equal comparison"""
    a = DualNumber(5, 2)
    b = DualNumber(3, 1)
    c = DualNumber(5, 1)

    assert a >= b
    assert a >= c
    assert a >= 3
    assert a >= 5
    assert not (b >= a)
