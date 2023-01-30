import check50

@check50.check()
def exists():
    """forloop.py exists."""
    check50.exists("forloop.py")


@check50.check(exists)
def result():
    """result is 55"""
    check50.run("python3 forloop.py").stdout("55").exit(0)
