def foo(a: int, b: int) -> int:
    return a + b * 2 - 140


# result = foo(12, 13)


def test_foo():
    a = 12
    b = 13
    result = foo(a, b)

    assert result == -101
