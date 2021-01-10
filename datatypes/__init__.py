import check50

@check50.check()
def exists():
    """datatypes.py exists."""
    check50.exists("datatypes.py")


@check50.check(exists)
def check_get_int():
    """datatypes.py contains get_ing=t"""

    app = open("datatypes.py").read()
    if 'get_int(' not in app:
        raise check50.Failure(f"missing get_int() in datatypes.py")

@check50.check(exists)
def check_get_float():
    """datatypes.py contains get_float"""

    app = open("datatypes.py").read()
    if 'get_float(' not in app:
        raise check50.Failure(f"missing get_float() in datatypes.py")
