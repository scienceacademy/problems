import check50

@check50.check()
def exists():
    """operators.py exists."""
    check50.exists("operators.py")


@check50.check(exists)
def check_add():
    """operators.py contains 'b = a + 3'"""

    app = open("operators.py").read()
    if 'b = a + 3' not in app:
        raise check50.Failure(f"missing addition assignment for 'b'")

@check50.check(exists)
def check_mult():
    """operators.py contains 'c = a * 5'"""

    app = open("operators.py").read()
    if 'c = a * 5' not in app:
        raise check50.Failure(f"missing mult. assignment for 'c'")


@check50.check(exists)
def check_div():
    """operators.py contains 'd = a / 4'"""

    app = open("operators.py").read()
    if 'd = a / 4' not in app:
        raise check50.Failure(f"missing div. assignment for 'd'")

@check50.check(exists)
def check_mod():
    """operators.py contains 'e = a % 4'"""

    app = open("operators.py").read()
    if 'e = a % 4' not in app:
        raise check50.Failure(f"missing remainder assignment for 'e'")

