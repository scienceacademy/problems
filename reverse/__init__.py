import check50
import check50.c


@check50.check()
def exists():
    """reverse.c exists"""
    check50.exists("reverse.c")


@check50.check(exists)
def compiles():
    """reverse.c compiles"""
    check50.c.compile("reverse.c", lcs50=True)


@check50.check(compiles)
def test0():
    """Check for reverse"""
    check50.run("./reverse").stdin("This is a test.").stdout(".tset a si sihT").exit(0)


