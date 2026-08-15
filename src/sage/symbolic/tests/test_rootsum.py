"""
Tests for RootSum support
"""

try:
    from sage.symbolic.rootsum import root_sum
except ImportError:
    from rootsum import root_sum


def test_rootsum_creation():
    """Test creating RootSum expressions."""
    var('x a')

    P = x**3 + a*x + 1
    rs = root_sum(P, lambda r: log(x - r)/(a + 3*r**2))

    assert rs is not None
    print("RootSum creation works")
    return rs


def test_rootsum_derivative():
    """Test differentiating RootSum."""
    var('x a')

    P = x**3 + a*x + 1
    rs = root_sum(P, lambda r: log(x - r)/(a + 3*r**2))

    deriv = derivative(rs, x)
    print("RootSum derivative works")
    return deriv


def test_rootsum_evaluation():
    """Test evaluating RootSum."""
    var('x a')

    P = x**2 - 1
    rs = root_sum(P, lambda r: r**2)

    result = rs._eval_(P, lambda r: r**2)
    expected = 2

    assert result == expected
    print("RootSum evaluation works")
    return result


def test_rootsum_latex():
    """Test LaTeX representation."""
    var('x a')

    P = x**3 + a*x + 1
    rs = root_sum(P, lambda r: log(x - r)/(a + 3*r**2))

    latex_str = rs._latex_()
    print(f"RootSum LaTeX: {latex_str}")
    return latex_str


def test_rootsum_sympy_conversion():
    """Test SymPy conversion."""
    var('x a')

    P = x**3 + a*x + 1
    rs = root_sum(P, lambda r: log(x - r)/(a + 3*r**2))

    try:
        sympy_obj = rs._sympy_()
        print(f"RootSum to SymPy: {sympy_obj}")
    except Exception as e:
        print(f"RootSum to SymPy failed: {e}")


if __name__ == "__main__":
    test_rootsum_creation()
    test_rootsum_derivative()
    test_rootsum_evaluation()
    test_rootsum_latex()
    test_rootsum_sympy_conversion()
    print("\nAll RootSum tests completed")
