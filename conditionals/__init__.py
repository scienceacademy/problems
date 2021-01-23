import check50

@check50.check()
def exists():
    """grades.py exists."""
    check50.exists("grades.py")


@check50.check(exists)
def testA():
    """responds to input of 95."""
    check50.run("python3 grades.py").stdin("95").stdout("You got an A!").exit(0)


@check50.check(exists)
def testB():
    """responds to input of 85."""
    check50.run("python3 grades.py").stdin("85").stdout("You got a B!").exit(0)


@check50.check(exists)
def testC():
    """responds to input of 75."""
    check50.run("python3 grades.py").stdin("75").stdout("You got a C!").exit(0)


@check50.check(exists)
def testA():
    """responds to input of 65."""
    check50.run("python3 grades.py").stdin("65").stdout("You got a D!").exit(0)

