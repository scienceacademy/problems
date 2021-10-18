import check50


@check50.check()
def exists():
    """error1-4.py exist."""
    check50.exists("error1.py")
    check50.exists("error2.py")
    check50.exists("error3.py")
    check50.exists("error4.py")


@check50.check(exists)
def test_p1():
    """error1.py produces the correct output."""
    check50.run("python3 error1.py").stdin("Wanda").stdout("Wanda").exit(0)


@check50.check(exists)
def test_p2():
    """error2.py outputs correctly with '10'."""
    check50.run("python3 error2.py").stdin("10").stdout("20").exit(0)


@check50.check(exists)
def test_p3a():
    """error3.py outputs correctly with '1'."""
    check50.run("python3 error3.py").stdin("1").stdout("1").exit(0)


@check50.check(exists)
def test_p3b():
    """error3.py outputs correctly with '2'."""
    check50.run("python3 error3.py").stdin("2").stdout("2").exit(0)


@check50.check(exists)
def test_p3c():
    """error3.py outputs correctly with '3'."""
    check50.run("python3 error3.py").stdin("3").stdout("3").exit(0)


@check50.check(exists)
def test_p4():
    """error4.py outputs correctly with '1, 2, 3, 4, 5'."""
    check50.run("python3 error4.py").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("120").exit(0)
