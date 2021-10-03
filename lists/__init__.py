import check50

@check50.check()
def exists():
    """smallest.py and odds.py exist."""
    check50.exists("smallest.py")
    check50.exists("odds.py")


@check50.check(exists)
def testA():
    """smallest.py outputs the correct smallest value."""
    check50.run("python3 smallest.py").stdout("4").exit(0)


@check50.check(exists)
def testB():
    """odds.py outputs correctly."""
    check50.run("python3 odds.py").stdout("4").exit(0)

