import check50

@check50.check()
def exists():
    """functions.py exists."""
    check50.exists("functions.py")


@check50.check(exists)
def resulta():
    """212 degrees F yields 100.0 degrees C"""
    check50.run("python3 functions.py").stdin("212.0").stdout("100.0").exit(0)

@check50.check(exists)
def resultb():
    """32 degrees F yields 0.0 degrees C"""
    check50.run("python3 functions.py").stdin("32.0").stdout("0.0").exit(0)


@check50.check(exists)
def resultc():
    """65.3 degrees F yields 18.5 degrees C"""
    check50.run("python3 functions.py").stdin("65.3").stdout("18.5").exit(0)


@check50.check(exists)
def resultd():
    """-40.0 degrees F yields -40.0 degrees C"""
    check50.run("python3 functions.py").stdin("-40.0").stdout("-40.0").exit(0)
