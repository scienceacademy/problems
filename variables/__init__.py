import check50

@check50.check()
def exists():
    """variables.py exists."""
    check50.exists("variables.py")

@check50.check(exists)
def test10():
    """responds to input of 10."""
    check50.run("python3 variables.py").stdin("10").stdout("20").exit(0)

@check50.check(exists)
def test21():
    """responds to 21."""
    check50.run("python3 variables.py").stdin("21").stdout("31").exit(0)
