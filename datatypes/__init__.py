import check50

@check50.check()
def exists():
    """datatypes.py exists."""
    check50.exists("datatypes.py")


@check50.check(exists)
def check_get_int():
    """datatypes.py contains int(input("""

    app = open("datatypes.py").read()
    if 'int(input(' not in app:
        raise check50.Failure(f"You need to convert input to an int")

@check50.check(exists)
def check_get_float():
    """datatypes.py contains float(input("""

    app = open("datatypes.py").read()
    if 'float(input(' not in app:
        raise check50.Failure(f"You need to convert input to a float")
