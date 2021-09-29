import check50

@check50.check()
def exists():
    """forloop.py and vowels.py exist."""
    check50.exists("forloop.py")
    check50.exists("vowels.py")


@check50.check(exists)
def result():
    """result is 55"""
    check50.run("python3 forloop.py").stdout("55").exit(0)


@check50.check(exists)
def testB():
    """string.py outputs correctly with 'aaron'."""
    check50.run("python3 vowels.py").stdin("aaron").stdout("3").exit(0)


@check50.check(exists)
def testC():
    """string.py outputs correctly with 'alexandria'."""
    check50.run("python3 vowels.py").stdin("alexandria").stdout("5").exit(0)