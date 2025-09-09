import check50
import check50.c


@check50.check()
def exists():
    """alphabetical.c exists"""
    check50.exists("alphabetical.c")


@check50.check(exists)
def compiles():
    """alphabetical.c compiles"""
    check50.c.compile("alphabetical.c", lcs50=True)


@check50.check(compiles)
def test0():
    """Check for alphabetical"""
    check50.run("./alphabetical").stdin("abcdefg").stdout("Yes").exit(0)


@check50.check(compiles)
def test1():
    """Check for not alphabetical"""
    check50.run("./alphabetical").stdin("gfedcba").stdout("No").exit(0)
