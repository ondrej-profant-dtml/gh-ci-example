from uv_p1.foo import bar


def test_dummy():
    assert True


def test_bar():
    assert bar() == "bar"
