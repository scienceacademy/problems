import check50

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Veronica."""
    check50.run("python hello.py").stdin("Veronica").stdout("Veronica")

@check50.check(compiles)
def brian():
    """responds to name Brian."""
    check50.run("python hello.py").stdin("Brian").stdout("Brian")
