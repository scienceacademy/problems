import check50

@check50.check()
def exists():
    """grades.py and odd_even.py exist."""
    check50.exists("grades.py")
    check50.exists("odd_even.py")


@check50.check(exists)
def testA():
    """grades.py responds to input of 95."""
    check50.run("python3 grades.py").stdin("95").stdout("You got an A!").exit(0)


@check50.check(exists)
def testB():
    """grades.py responds to input of 85."""
    check50.run("python3 grades.py").stdin("85").stdout("You got a B!").exit(0)


@check50.check(exists)
def testC():
    """grades.py responds to input of 75."""
    check50.run("python3 grades.py").stdin("75").stdout("You got a C!").exit(0)


@check50.check(exists)
def testA():
    """grades.py responds to input of 65."""
    check50.run("python3 grades.py").stdin("65").stdout("You got a D!").exit(0)


@check50.check(exists)
def test_even():
    """odd_even.py responds to input of 8."""
    actual = check50.run("python3 odd_even.py").stdin("8").stdout()
    if "Odd" in actual:
        raise check50.Mismatch("Even", actual)


@check50.check(exists)
def test_even2():
    """odd_even.py responds to input of 7."""
    check50.run("python3 odd_even.py").stdin("7").stdout("Odd", regex=False).exit(0)


@check50.check(exists)
def test_odd():
    """odd_even.py responds to input of 11."""
    check50.run("python3 odd_even.py").stdin("11").stdout("Odd", regex=False).exit(0)


@check50.check(exists)
def test_zero():
    """odd_even.py responds to input of 0."""
    check50.run("python3 odd_even.py").stdin("0").stdout("Even", regex=False).exit(0)
