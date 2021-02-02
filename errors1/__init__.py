import check50


@check50.check()
def exists():
    """p1-4.py exist."""
    check50.exists("p1.py")
    check50.exists("p2.py")
    check50.exists("p3.py")
    check50.exists("p4.py")


@check50.check(exists)
def test_p1():
    """p1.py produces the correct output."""
    check50.run("python3 p1.py").stdin("Wanda").stdout("Wanda").exit(0)


@check50.check(exists)
def test_p2():
    """p2.py outputs correctly with '10'."""
    check50.run("python3 p2.py").stdin("10").stdout("20").exit(0)


@check50.check(exists)
def test_p3a():
    """p3.py outputs correctly with '1'."""
    check50.run("python3 p3.py").stdin("1").stdout("1").exit(0)


@check50.check(exists)
def test_p3b():
    """p3.py outputs correctly with '2'."""
    check50.run("python3 p3.py").stdin("2").stdout("2").exit(0)


@check50.check(exists)
def test_p3c():
    """p3.py outputs correctly with '3'."""
    check50.run("python3 p3.py").stdin("3").stdout("3").exit(0)


@check50.check(exists)
def test_p4():
    """p4.py outputs correctly with '1, 2, 3, 4, 5'."""
    check50.run("python3 p4.py").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("120").exit(0)
