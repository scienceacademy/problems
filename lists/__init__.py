import check50

@check50.check()
def exists():
    """list.py and string.py exist."""
    check50.exists("list.py")
    check50.exists("string.py")


@check50.check(exists)
def testA():
    """list.py outputs the correct squared values."""
    check50.run("python3 list.py").stdout("[4, 49, 16, 25, 81]").exit(0)


@check50.check(exists)
def testB():
    """string.py outputs correctly with 'aaron'."""
    check50.run("python3 string.py").stdin("aaron").stdout("3").exit(0)


@check50.check(exists)
def testC():
    """string.py outputs correctly with 'alexandria'."""
    check50.run("python3 string.py").stdin("alexandria").stdout("5").exit(0)
